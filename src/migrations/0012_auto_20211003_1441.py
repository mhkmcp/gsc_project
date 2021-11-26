# Generated by Django 3.1.3 on 2021-10-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0011_auto_20211003_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, default='', max_length=63),
        ),
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(blank=True, default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='member',
            name='current_address',
            field=models.CharField(blank=True, default='', max_length=63),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='father_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='fb_link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='mother_name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='passport',
            field=models.CharField(blank=True, default='', max_length=63),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='member',
            name='whatsapp_number',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]
