# Generated by Django 2.2 on 2020-05-20 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.CharField(default='', max_length=64, verbose_name='이메일'),
        ),
    ]
