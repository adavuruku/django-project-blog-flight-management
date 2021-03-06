# Generated by Django 4.0.2 on 2022-02-26 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=240)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='firstApp.customer')),
            ],
        ),
    ]
