# Generated by Django 2.2.5 on 2019-09-09 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20190909_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='seats_left',
            field=models.IntegerField(default=0),
        ),
    ]
