# Generated by Django 5.1 on 2025-03-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subdread', '0009_alter_subdread_banner_alter_subdread_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subdread',
            name='banner',
            field=models.ImageField(blank=True, default='/images/banner/default_banner.png', null=True, upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='subdread',
            name='icon',
            field=models.ImageField(blank=True, default='/images/icon/default_icon.png', null=True, upload_to='icon'),
        ),
    ]
