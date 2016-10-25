# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ba_namotswe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adherencecounselling',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='artregimen',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='arvhistory',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='assessmenthistory',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='crfmetadata',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='death',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='extraction',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='extractionchecklist',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='historicalsubjectconsent',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='oi',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='packinglist',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='pregnancyhistory',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='registeredsubject',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='requisitionmetadata',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectconsent',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectrequisition',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='subjectvisit',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='tbhistory',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='transferhistory',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='hostname_created',
            field=models.CharField(default='kmotingwa', editable=False, help_text='System field. (modified on create only)', max_length=50),
        ),
    ]
