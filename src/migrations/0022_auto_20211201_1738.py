# Generated by Django 3.1.3 on 2021-12-01 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0021_educationscholarship_medicalassistance_trainingassistance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainingassistance',
            old_name='dutation',
            new_name='duration',
        ),
    ]
