# Generated by Django 2.2 on 2020-05-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_title', models.CharField(default='', max_length=20, null=True)),
                ('subject_point', models.IntegerField(null=True)),
                ('subject_code', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
    ]
