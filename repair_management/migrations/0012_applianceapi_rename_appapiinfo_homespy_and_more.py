# Generated by Django 5.1.1 on 2024-10-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair_management', '0011_alter_appliance_cost_alter_appliance_exp_end_of_life'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplianceApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('category_name', models.CharField(max_length=50, null=True)),
                ('detail_category_name', models.CharField(max_length=250, null=True)),
                ('color', models.CharField(max_length=30, null=True)),
                ('product_image', models.CharField(max_length=250, null=True)),
                ('product_doc_1', models.CharField(max_length=250, null=True)),
                ('product_doc_2', models.CharField(max_length=250, null=True)),
                ('lowest_listed_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('home_depot_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('msrp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='AppApiInfo',
            new_name='HomeSpy',
        ),
        migrations.RemoveField(
            model_name='appliance',
            name='serial_number',
        ),
    ]
