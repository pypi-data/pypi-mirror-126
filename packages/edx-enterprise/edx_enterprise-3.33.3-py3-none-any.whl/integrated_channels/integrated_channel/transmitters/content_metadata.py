# -*- coding: utf-8 -*-
"""
Generic content metadata transmitter for integrated channels.
"""

import json
import logging
from datetime import datetime
from itertools import islice

from django.apps import apps
from django.conf import settings

from integrated_channels.exceptions import ClientError
from integrated_channels.integrated_channel.client import IntegratedChannelApiClient
from integrated_channels.integrated_channel.transmitters import Transmitter
from integrated_channels.utils import chunks

LOGGER = logging.getLogger(__name__)


class ContentMetadataTransmitter(Transmitter):
    """
    Used to transmit content metadata to an integrated channel.
    """

    def __init__(self, enterprise_configuration, client=IntegratedChannelApiClient):
        """
        By default, use the abstract integrated channel API client which raises an error when used if not subclassed.
        """
        super().__init__(
            enterprise_configuration=enterprise_configuration,
            client=client
        )

    def transmit(self, create_payload, update_payload, delete_payload, content_updated_mapping, **kwargs):
        """
        Transmit content metadata items to the integrated channel. Save or update content metadata records according to
        the type of transmission.
        """
        LOGGER.info(
            f'Transmitting delete payload: {delete_payload} for customer: '
            f'{self.enterprise_configuration.enterprise_customer.uuid}'
        )
        self._transmit_delete(delete_payload)

        LOGGER.info(
            f'Transmitting create payload: {create_payload} for customer: '
            f'{self.enterprise_configuration.enterprise_customer.uuid}'
        )
        self._transmit_create(create_payload, content_updated_mapping)

        LOGGER.info(
            f'Transmitting update payload: {update_payload} for customer: '
            f'{self.enterprise_configuration.enterprise_customer.uuid}'
        )
        self._transmit_update(update_payload)

    def _prepare_items_for_transmission(self, channel_metadata_items):
        """
        Perform any necessary modifications to content metadata item
        data structure before transmission. This can be overridden by
        subclasses to add any data structure wrappers expected by the
        integrated channel.
        """
        return channel_metadata_items

    def _serialize_items(self, channel_metadata_items):
        """
        Serialize content metadata items for a create transmission to the integrated channel.
        """
        return json.dumps(
            self._prepare_items_for_transmission(channel_metadata_items),
            sort_keys=True
        ).encode('utf-8')

    def _transmit_create(self, channel_metadata_item_map, content_updated_mapping):
        """
        Transmit content metadata creation to integrated channel.
        """
        chunk_items = chunks(channel_metadata_item_map, self.enterprise_configuration.transmission_chunk_size)
        transmission_limit = settings.INTEGRATED_CHANNELS_API_CHUNK_TRANSMISSION_LIMIT.get(
            self.enterprise_configuration.channel_code()
        )
        for chunk in islice(chunk_items, transmission_limit):
            serialized_chunk = self._serialize_items(list(chunk.values()))
            try:
                self.client.create_content_metadata(serialized_chunk)
            except ClientError as exc:
                LOGGER.error(
                    'Failed to create [%s] content metadata items for integrated channel [%s] [%s]. '
                    'Task failed with message [%s] and status code [%s]',
                    len(chunk),
                    self.enterprise_configuration.enterprise_customer.name,
                    self.enterprise_configuration.channel_code(),
                    exc.message,
                    exc.status_code
                )
                LOGGER.exception(exc)
            else:
                self._create_transmissions(chunk, content_updated_mapping)

    def _transmit_update(self, update_payload):
        """
        Transmit content metadata update to integrated channel.
        """
        updated_metadata_mapping = {key: item.channel_metadata for key, item in update_payload.items()}
        chunk_items = chunks(updated_metadata_mapping, self.enterprise_configuration.transmission_chunk_size)
        transmission_limit = settings.INTEGRATED_CHANNELS_API_CHUNK_TRANSMISSION_LIMIT.get(
            self.enterprise_configuration.channel_code()
        )
        for chunk in islice(chunk_items, transmission_limit):
            serialized_chunk = self._serialize_items(list(chunk.values()))
            try:
                self.client.update_content_metadata(serialized_chunk)
            except ClientError as exc:
                LOGGER.error(
                    'Failed to update [%s] content metadata items for integrated channel [%s] [%s]. '
                    'Task failed with message [%s] and status code [%s]',
                    len(chunk),
                    self.enterprise_configuration.enterprise_customer.name,
                    self.enterprise_configuration.channel_code(),
                    exc.message,
                    exc.status_code
                )
                LOGGER.exception(exc)
            else:
                self._update_transmissions(update_payload, chunk)

    def _transmit_delete(self, channel_metadata_item_map):
        """
        Transmit content metadata deletion to integrated channel.
        """
        items_to_delete = {key: item.channel_metadata for key, item in channel_metadata_item_map.items()}
        chunk_items = chunks(items_to_delete, self.enterprise_configuration.transmission_chunk_size)
        transmission_limit = settings.INTEGRATED_CHANNELS_API_CHUNK_TRANSMISSION_LIMIT.get(
            self.enterprise_configuration.channel_code()
        )
        for chunk in islice(chunk_items, transmission_limit):
            serialized_chunk = self._serialize_items(list(chunk.values()))
            try:
                self.client.delete_content_metadata(serialized_chunk)
            except ClientError as exc:
                LOGGER.error(
                    'Failed to delete [%s] content metadata items for integrated channel [%s] [%s]. '
                    'Task failed with message [%s] and status code [%s]',
                    len(chunk),
                    self.enterprise_configuration.enterprise_customer.name,
                    self.enterprise_configuration.channel_code(),
                    exc.message,
                    exc.status_code
                )
                LOGGER.exception(exc)
            else:
                self._delete_transmissions(chunk.keys())

    def _create_transmissions(self, content_metadata_item_map, content_updated_mapping):
        """
        Create ContentMetadataItemTransmission models for the given content metadata items.
        """
        ContentMetadataItemTransmission = apps.get_model(
            'integrated_channel',
            'ContentMetadataItemTransmission'
        )
        create_transmissions = []
        reactivate_transmissions = []
        for content_id, channel_metadata in content_metadata_item_map.items():
            LOGGER.info(
                f'Creating content transmission record for course: {content_id} under enterprise customer: '
                f'{self.enterprise_configuration.enterprise_customer.uuid}.'
            )
            past_deleted_transmission = ContentMetadataItemTransmission.objects.filter(
                enterprise_customer=self.enterprise_configuration.enterprise_customer,
                integrated_channel_code=self.enterprise_configuration.channel_code(),
                content_id=content_id,
                deleted_at__isnull=False,
            )

            if past_deleted_transmission.first():
                LOGGER.info(
                    f'Found previously deleted content record while creating record for course: {content_id}'
                    f'under customer: {self.enterprise_configuration.enterprise_customer.uuid}'
                )
                past_deleted_transmission.deleted_at = None
                past_deleted_transmission.channel_metadata = channel_metadata
                past_deleted_transmission.content_last_changed = content_updated_mapping.get(content_id)
                past_deleted_transmission.enterprise_customer_catalog_uuid = content_updated_mapping.get(
                    content_id
                ).get('catalog_uuid')
                reactivate_transmissions.append(past_deleted_transmission.save())

            else:
                # Does there exist a record under a different catalog uuid?
                past_transmission = ContentMetadataItemTransmission.objects.filter(
                    enterprise_customer=self.enterprise_configuration.enterprise_customer,
                    integrated_channel_code=self.enterprise_configuration.channel_code(),
                    content_id=content_id,
                    deleted_at__isnull=True,
                )
                if past_transmission:
                    past_transmission.channel_metadata = channel_metadata
                    past_transmission.content_last_changed = content_updated_mapping.get(content_id)
                    past_transmission.enterprise_customer_catalog_uuid = content_updated_mapping.get(content_id).get(
                        'catalog_uuid'
                    )
                    reactivate_transmissions.append(past_transmission.save())
                else:
                    create_transmissions.append(
                        ContentMetadataItemTransmission(
                            enterprise_customer=self.enterprise_configuration.enterprise_customer,
                            integrated_channel_code=self.enterprise_configuration.channel_code(),
                            content_id=content_id,
                            channel_metadata=channel_metadata,
                            content_last_changed=content_updated_mapping.get(content_id).get('modified'),
                            enterprise_customer_catalog_uuid=content_updated_mapping.get(content_id).get('catalog_uuid')
                        )
                    )

        ContentMetadataItemTransmission.objects.bulk_create(create_transmissions, ignore_conflicts=True)
        ContentMetadataItemTransmission.objects.bulk_update(
            reactivate_transmissions,
            ['deleted_at', 'channel_metadata', 'content_last_changed'],
        )

    def _update_transmissions(self, update_payload, content_metadata_item_map):
        """
        Update ContentMetadataItemTransmission models for the given content metadata items.
        """
        for content_id in content_metadata_item_map.keys():
            transmission = update_payload.get(content_id)
            if transmission:
                LOGGER.info(
                    f'Updating content transmission record for course: {content_id} under enterprise customer: '
                    f'{self.enterprise_configuration.enterprise_customer.uuid}.'
                )
                transmission.save()

    def _delete_transmissions(self, content_metadata_item_ids):
        """
        Delete ContentMetadataItemTransmission models associated with the given content metadata items.
        """
        ContentMetadataItemTransmission = apps.get_model(
            'integrated_channel',
            'ContentMetadataItemTransmission'
        )
        LOGGER.info(
            f'Marking content transmission record for courses: {content_metadata_item_ids} as deleted for customer: '
            f'{self.enterprise_configuration.enterprise_customer.uuid}'
        )
        ContentMetadataItemTransmission.objects.filter(
            enterprise_customer=self.enterprise_configuration.enterprise_customer,
            integrated_channel_code=self.enterprise_configuration.channel_code(),
            content_id__in=content_metadata_item_ids,
        ).update(deleted_at=datetime.now())
