# Generated by Django 2.2.5 on 2019-09-09 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_seats_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='seats_left',
            field=models.IntegerField(),
        ),
    ]
