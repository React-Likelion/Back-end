# Generated by Django 4.0.6 on 2022-08-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='members',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='members',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='identification',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
