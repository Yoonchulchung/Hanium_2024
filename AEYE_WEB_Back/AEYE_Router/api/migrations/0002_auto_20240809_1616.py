# Generated by Django 3.2 on 2024-08-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aeye_wno_models',
            name='message',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='aeye_wno_models',
            name='operation',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='aeye_wno_models',
            name='whoami',
            field=models.CharField(max_length=40),
        ),
    ]
