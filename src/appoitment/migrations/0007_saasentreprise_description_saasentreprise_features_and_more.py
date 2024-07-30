# Generated by Django 4.0 on 2024-07-24 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitment', '0006_saasentreprise_rename_document_modeledocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='saasentreprise',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='saasentreprise',
            name='features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='saasentreprise',
            name='status',
            field=models.CharField(choices=[('actif', 'Actif'), ('maintenance', 'En maintenance')], default='actif', max_length=50),
        ),
    ]
