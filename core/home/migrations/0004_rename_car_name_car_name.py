# Generated by Django 5.1.4 on 2025-01-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_name',
            new_name='name',
        ),
    ]