# Generated by Django 3.0.6 on 2020-06-01 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_status_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='n_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='status',
            name='n_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='status',
            name='n_shares',
            field=models.IntegerField(default=0),
        ),
    ]
