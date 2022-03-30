# Generated by Django 3.1.3 on 2022-03-30 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0008_auto_20220329_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('headmaster', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('school_code', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('stablished_at', models.DateField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mosque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('imam', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('stablished_at', models.DateField(blank=True, default='', null=True)),
            ],
        ),
    ]
