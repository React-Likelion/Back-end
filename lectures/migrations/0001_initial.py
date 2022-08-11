# Generated by Django 4.0.6 on 2022-08-11 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0008_user_delete_members'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollStudents',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'enroll',
            },
        ),
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('youtube_link', models.CharField(max_length=255)),
                ('image', models.FileField(upload_to='images')),
                ('main_category', models.CharField(choices=[('미술', '미술'), ('요리', '요리'), ('음악', '음악'), ('운동', '운동'), ('외국어', '외국어'), ('사진/영상', '사진/영상'), ('창업/부업', '창업/부업'), ('프로그래밍', '프로그래밍'), ('금융/제테크', '금융/제테크'), ('라이프스타일', '라이프스타일'), ('비즈니스/마케팅', '비즈니스/마케팅')], max_length=10)),
                ('sub_category', models.CharField(choices=[('영어', '영어'), ('제2외국어', '제2외국어'), ('그림', '그림'), ('공예', '공예'), ('디자인', '디자인'), ('미술 기타', '기타'), ('요리', '요리'), ('베이킹', '베이킹'), ('음료/주류', '음료/주류'), ('요가/필라테스', '요가/필라테스'), ('헬스', '헬스'), ('운동 기타', '기타'), ('웹/앱', '웹/앱'), ('IT교양', 'IT교양'), ('법률', '법률'), ('상담', '상담'), ('뷰티', '뷰티'), ('라이프스타일 기타', '기타'), ('부동산', '부동산'), ('주식', '주식'), ('제테크', '제테크')], max_length=10)),
                ('enroll_cnt', models.IntegerField(default=0)),
                ('like_cnt', models.IntegerField(default=0)),
                ('visit_cnt', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('enroll_students', models.ManyToManyField(blank=True, related_name='enroll_students', through='lectures.EnrollStudents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'lectures',
            },
        ),
        migrations.CreateModel(
            name='LikeMembers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lectures', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_lectures', to='lectures.lectures')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL, to_field='nickname')),
            ],
            options={
                'db_table': 'like',
            },
        ),
        migrations.AddField(
            model_name='lectures',
            name='like_members',
            field=models.ManyToManyField(blank=True, related_name='like_members', through='lectures.LikeMembers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lectures',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL, to_field='nickname'),
        ),
        migrations.AddField(
            model_name='enrollstudents',
            name='lectures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enroll_lectures', to='lectures.lectures'),
        ),
        migrations.AddField(
            model_name='enrollstudents',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enroll_user', to=settings.AUTH_USER_MODEL, to_field='nickname'),
        ),
    ]