# Generated by Django 4.0.6 on 2022-08-04 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentorings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255, null=True)),
                ('field', models.CharField(max_length=255, null=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('age_group', models.IntegerField()),
                ('limit', models.IntegerField()),
                ('tag', models.CharField(max_length=255, null=True)),
                ('image', models.CharField(max_length=255, null=True)),
                ('member', models.CharField(max_length=255, null=True)),
                ('member_cnt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mentoring_chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('mentorings_id', models.ForeignKey(db_column='mentorings_id', on_delete=django.db.models.deletion.CASCADE, to='mentorings.mentorings')),
            ],
        ),
    ]
