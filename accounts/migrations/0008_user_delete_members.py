# Generated by Django 4.0.6 on 2022-08-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_is_admin_members_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('identification', models.CharField(max_length=11, unique=True)),
                ('name', models.CharField(max_length=11)),
                ('nickname', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birth', models.DateField()),
                ('job', models.CharField(choices=[('1', '관리자'), ('2', '전문가 및 관련 종사자'), ('3', '사무 종사자'), ('4', '서비스 종사자'), ('5', '판매 종사자'), ('6', '농림 어업 숙련 종사자'), ('7', '기은원 및 관련 기능 종사자'), ('8', '장치 기계 조작 및 조립 종사자'), ('9', '단순 노무 종사자'), ('10', '군인 및 학생'), ('11', '없음')], max_length=2)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]