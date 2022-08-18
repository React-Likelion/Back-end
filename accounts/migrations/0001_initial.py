# Generated by Django 4.0.6 on 2022-08-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('plus_log', models.TextField(blank=True, null=True)),
                ('minus_log', models.TextField(blank=True, null=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
            ],
        ),
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
                ('job', models.CharField(choices=[('관리자', '관리자'), ('전문가 및 관련 종사자', '전문가 및 관련 종사자'), ('사무 종사자', '사무 종사자'), ('서비스 종사자', '서비스 종사자'), ('판매 종사자', '판매 종사자'), ('농림 어업 숙련 종사자', '농림 어업 숙련 종사자'), ('기은원 및 관련 기능 종사자', '기은원 및 관련 기능 종사자'), ('장치 기계 조작 및 조립 종사자', '장치 기계 조작 및 조립 종사자'), ('단순 노무 종사자', '단순 노무 종사자'), ('군인 및 학생', '군인 및 학생'), ('없음', '없음')], max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, unique=True, upload_to='accounts/')),
                ('point', models.IntegerField(default=10000)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('log', models.ManyToManyField(blank=True, to='accounts.logs')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
