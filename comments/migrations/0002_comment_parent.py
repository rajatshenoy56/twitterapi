# Generated by Django 3.0.6 on 2020-05-31 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_status_user'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='status.Status'),
        ),
    ]
