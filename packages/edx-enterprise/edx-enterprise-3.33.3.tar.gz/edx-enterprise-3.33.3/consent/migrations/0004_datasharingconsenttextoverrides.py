# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 11:28


import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0001_squashed_0092_auto_20200312_1650'),
        ('consent', '0003_historicaldatasharingconsent_history_change_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSharingConsentTextOverrides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('page_title', models.CharField(help_text='Title of page', max_length=255)),
                ('left_sidebar_text', models.TextField(blank=True, help_text='Fill in a text for left sidebar paragraph. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>platform_name: Name of platform.</li><li>item: A string which is "course" or "program" depending on the type of consent.</li><li>course_title: Title of course. Available when type of consent is course.</li><li>course_start_date: Course start date. Available when type of consent is course.</li></ul>', null=True)),
                ('top_paragraph', models.TextField(blank=True, help_text='Fill in a text for first paragraph of page. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>platform_name: Name of platform.</li><li>item: A string which is "course" or "program" depending on the type of consent.</li><li>course_title: Title of course. Available when type of consent is course.</li><li>course_start_date: Course start date. Available when type of consent is course.</li></ul>', null=True)),
                ('agreement_text', models.TextField(blank=True, help_text='Text next to agreement check mark', null=True)),
                ('continue_text', models.CharField(help_text='Text of agree button', max_length=255)),
                ('abort_text', models.CharField(help_text='Text of decline link', max_length=255)),
                ('policy_dropdown_header', models.CharField(blank=True, help_text='Text of policy drop down', max_length=255, null=True)),
                ('policy_paragraph', models.TextField(blank=True, help_text='Fill in a text for policy paragraph at the bottom of page. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>platform_name: Name of platform.</li><li>item: A string which is "course" or "program" depending on the type of consent.</li><li>course_title: Title of course. Available when type of consent is course.</li><li>course_start_date: Course start date. Available when type of consent is course.</li></ul>', null=True)),
                ('confirmation_modal_header', models.CharField(help_text='Heading text of dialog box which appears when user decline to provide consent', max_length=255)),
                ('confirmation_modal_text', models.TextField(help_text='Fill in a text for dialog which appears when user decline to provide consent. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>item: A string which is "course" or "program" depending on the type of consent.</li><li>course_title: Title of course. Available when type of consent is course.</li><li>course_start_date: Course start date. Available when type of consent is course.</li></ul>')),
                ('modal_affirm_decline_text', models.CharField(help_text='Text of decline button on confirmation dialog box', max_length=255)),
                ('modal_abort_decline_text', models.CharField(help_text='Text of abort decline link on confirmation dialog box', max_length=255)),
                ('declined_notification_title', models.TextField(help_text='Fill in a text for title of the notification which appears on dashboard when user decline to provide consent. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>course_title: Title of course. Available when type of consent is course.</li></ul>')),
                ('declined_notification_message', models.TextField(help_text='Fill in a text for message of the notification which appears on dashboard when user decline to provide consent. The following variables may be available:<br /><ul><li>enterprise_customer_name: A name of enterprise customer.</li><li>course_title: Title of course. Available when type of consent is course.</li></ul>')),
                ('published', models.BooleanField(default=False, help_text='Specifies whether data sharing consent page is published.')),
                ('enterprise_customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data_sharing_consent_page', to='enterprise.EnterpriseCustomer')),
            ],
            options={
                'verbose_name_plural': 'Data sharing consent text overrides',
            },
        ),
    ]
