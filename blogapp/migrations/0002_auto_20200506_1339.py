# Generated by Django 2.2 on 2020-05-06 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='calculator',
            name='subject',
        ),
    ]
