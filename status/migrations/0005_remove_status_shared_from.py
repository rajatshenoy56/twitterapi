# Generated by Django 3.0.6 on 2020-06-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_status_shared_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='shared_from',
        ),
    ]
