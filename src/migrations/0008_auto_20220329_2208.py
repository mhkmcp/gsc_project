# Generated by Django 3.1.3 on 2022-03-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_auto_20220329_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='passport',
            field=models.CharField(max_length=63, unique=True),
        ),
    ]
