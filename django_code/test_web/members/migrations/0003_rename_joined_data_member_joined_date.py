# Generated by Django 4.1.7 on 2023-02-23 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_data_member_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='joined_data',
            new_name='joined_date',
        ),
    ]
