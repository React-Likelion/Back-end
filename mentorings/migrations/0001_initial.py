
# Generated by Django 4.0.6 on 2022-08-15 22:46


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mentorings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(choices=[('서울특별시', '서울특별시'), ('부산광역시', '부산광역시'), ('대구광역시', '대구광역시'), ('인천광역시', '인천광역시'), ('광주광역시', '광주광역시'), ('대전광역시', '대전광역시'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('제주특별자치도', '제주특별자치도')], max_length=20)),
                ('field', models.CharField(choices=[('외국어', '외국어'), ('미술', '미술'), ('요가/필라테스', '요가/필라테스'), ('헬스', '헬스'), ('법률', '법률'), ('상담', '상담'), ('뷰티', '뷰티'), ('프로그래밍', '프로그래밍'), ('비즈니스/마케팅', '비즈니스/마케팅'), ('사진/영상', '사진/영상'), ('부동산', '부동산'), ('주식', '주식'), ('재테크', '재테크'), ('창업/부업', '창업/부업')], max_length=20, null=True)),
                ('title', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('age_group', models.CharField(max_length=255, null=True)),
                ('limit', models.IntegerField(default=0, null=True)),
                ('tag', models.CharField(max_length=255, null=True)),
                ('tag2', models.CharField(max_length=255, null=True)),
                ('tag3', models.CharField(max_length=255, null=True)),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('member_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='mentoringsTouser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentorings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentoringsTouser', to='mentorings.mentorings')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentoringsTouser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mentorings',
            name='User',
            field=models.ManyToManyField(related_name='Member', through='mentorings.mentoringsTouser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mentorings',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='mentoring_chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('mentorings_id', models.ForeignKey(db_column='mentorings_id', on_delete=django.db.models.deletion.CASCADE, to='mentorings.mentorings')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
