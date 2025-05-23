# Generated by Django 5.2 on 2025-04-06 08:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subdread', '0011_rule'),
    ]

    operations = [
        migrations.AddField(
            model_name='flair',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flair',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rule',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
