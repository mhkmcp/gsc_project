# Generated by Django 3.1.3 on 2021-12-01 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0023_auto_20211201_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalassistance',
            old_name='bedget',
            new_name='budget',
        ),
    ]
