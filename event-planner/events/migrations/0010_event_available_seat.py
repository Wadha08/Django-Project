# Generated by Django 2.2.5 on 2019-09-09 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_remove_event_seats_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available_seat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]