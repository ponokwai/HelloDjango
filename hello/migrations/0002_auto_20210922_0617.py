# Generated by Django 3.2.7 on 2021-09-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='age',
            field=models.SmallIntegerField(null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='logmessage',
            name='first_name',
            field=models.CharField(max_length=500, null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='logmessage',
            name='last_name',
            field=models.CharField(max_length=500, null='true'),
            preserve_default='true',
        ),
    ]
