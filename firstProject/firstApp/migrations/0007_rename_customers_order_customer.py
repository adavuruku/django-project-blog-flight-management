# Generated by Django 4.0.2 on 2022-02-26 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0006_customer_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customers',
            new_name='customer',
        ),
    ]
