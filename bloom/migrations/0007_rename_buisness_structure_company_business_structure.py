# Generated by Django 3.2.6 on 2021-08-25 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloom', '0006_rename_contacts_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='buisness_structure',
            new_name='business_structure',
        ),
    ]