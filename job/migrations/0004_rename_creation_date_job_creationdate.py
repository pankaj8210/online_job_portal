# Generated by Django 3.2.8 on 2021-11-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='creation_date',
            new_name='creationdate',
        ),
    ]
