# Generated by Django 4.1.2 on 2022-11-11 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_name_car_carname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='carName',
            new_name='car_name',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='dateOfPurchase',
            new_name='date_of_purchase',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='topSpeed',
            new_name='top_speed',
        ),
    ]