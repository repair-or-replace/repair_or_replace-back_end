# Generated by Django 5.1.1 on 2024-10-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_management', '0005_rename_productinfo_appapiinfo_property_default_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appapiinfo',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appapiinfo',
            name='description',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appapiinfo',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
