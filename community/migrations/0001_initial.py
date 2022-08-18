<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-08-18 20:05
=======
# Generated by Django 4.0.6 on 2022-08-17 10:54
>>>>>>> f126263 (CREATE mainpage, mypage, point, UPDATE community)

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='community/')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('category', models.CharField(choices=[('공지', '공지'), ('정보', '정보'), ('자유', '자유')], max_length=10)),
                ('comment_cnt', models.IntegerField(default=0)),
<<<<<<< HEAD
                ('writer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_writerid', to=settings.AUTH_USER_MODEL)),
                ('writer_nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_writer', to=settings.AUTH_USER_MODEL, to_field='nickname')),
=======
                ('writer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_writer', to=settings.AUTH_USER_MODEL, to_field='nickname')),
                ('writer_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_writer_image', to=settings.AUTH_USER_MODEL, to_field='image', unique=True)),
>>>>>>> f126263 (CREATE mainpage, mypage, point, UPDATE community)
            ],
            options={
                'db_table': 'community',
            },
        ),
        migrations.CreateModel(
            name='CommunityComments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DT')),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board', to='community.community')),
                ('comment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='community.communitycomments')),
<<<<<<< HEAD
                ('writer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writerid', to=settings.AUTH_USER_MODEL)),
                ('writer_nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writer', to=settings.AUTH_USER_MODEL, to_field='nickname')),
=======
                ('writer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writer', to=settings.AUTH_USER_MODEL, to_field='nickname')),
                ('writer_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writer_image', to=settings.AUTH_USER_MODEL, to_field='image', unique=True)),
>>>>>>> f126263 (CREATE mainpage, mypage, point, UPDATE community)
            ],
            options={
                'db_table': 'communitycomments',
            },
        ),
    ]