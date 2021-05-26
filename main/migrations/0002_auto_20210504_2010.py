# Generated by Django 3.2 on 2021-05-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DotaResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OverwatchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='talantuser',
            name='cs_result',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.csresult'),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='dota_result',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dotaresult'),
        ),
        migrations.AddField(
            model_name='talantuser',
            name='overwatch_result',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.overwatchresult'),
        ),
    ]
