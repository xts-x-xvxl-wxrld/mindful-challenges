# Generated by Django 4.2.1 on 2023-08-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0004_alter_challenge_time_duration_alter_challenge_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='time_duration',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='customchallenge',
            name='time_duration',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='customchallenge',
            name='title',
            field=models.CharField(),
        ),
    ]