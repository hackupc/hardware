# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-10-05 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_auto_20180923_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='lending',
            new_name='borrowing',
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='borrowing_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hardware_admin_borrowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
