# Generated by Django 4.1.7 on 2023-04-01 15:56

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("application", "0006_alter_owner_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="owner",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None, unique=True
            ),
        ),
    ]