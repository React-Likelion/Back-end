# Generated by Django 4.0.6 on 2022-08-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorings', '0002_locations_alter_mentoring_chats_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorings',
            name='member_cnt',
            field=models.IntegerField(null=True),
        ),
    ]
