# Generated by Django 4.2.4 on 2023-08-28 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_name_userprofile_username_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='USERNAME_FIELD',
            new_name='name',
        ),
    ]
