# Generated by Django 2.2.5 on 2019-09-09 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='events.Event'),
        ),
    ]
