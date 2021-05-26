# Generated by Django 3.2 on 2021-05-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210504_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='talantuser',
            name='blizzard_access_token',
            field=models.CharField(default=None, max_length=2500, null=True),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='blizzard_battletag',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='steam_openid',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]