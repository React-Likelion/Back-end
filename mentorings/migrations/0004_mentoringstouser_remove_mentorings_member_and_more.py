# Generated by Django 4.0.6 on 2022-08-07 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentorings', '0003_alter_mentorings_member_cnt'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentoringsTouser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='mentorings',
            name='member',
        ),
        migrations.AddField(
            model_name='mentorings',
            name='User',
            field=models.ManyToManyField(related_name='Member', through='mentorings.mentoringsTouser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mentoringstouser',
            name='mentorings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentoringsTouser', to='mentorings.mentorings'),
        ),
        migrations.AddField(
            model_name='mentoringstouser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentoringsTouser', to=settings.AUTH_USER_MODEL),
        ),
    ]