# Generated by Django 4.0.3 on 2023-06-29 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitment', '0002_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='encryption_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
