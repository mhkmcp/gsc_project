# Generated by Django 3.1.3 on 2021-11-04 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0014_member_is_agreed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
    ]
