# Generated by Django 3.2 on 2021-05-25 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210525_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csresult',
            name='kd',
        ),
    ]
