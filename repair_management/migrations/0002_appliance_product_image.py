# Generated by Django 5.1.1 on 2024-11-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliance',
            name='product_image',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
