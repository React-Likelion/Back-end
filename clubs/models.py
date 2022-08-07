from django.db import models

from accounts.models import Members

FIELDS = [
    ('1', '관리자'),
    ('2', '전문가 및 관련 종사자'),
    ('3', '사무 종사자'),
    ('4', '서비스 종사자'),
    ('5', '판매 종사자'),
    ('6', '농림 어업 숙련 종사자'),
    ('7', '기은원 및 관련 기능 종사자'),
    ('8', '장치 기계 조작 및 조립 종사자'),
    ('9', '단순 노무 종사자'),
    ('10', '군인 및 학생'),
]

LOCATIIONS = [
    ('1', '경기도'),
    ('2', '강원도'),
    ('3', '충청북도'),
    ('4', '충청남도'),
    ('5', '전라북도'),
    ('6', '전라남도'),
    ('7', '경상북도'),
    ('8', '경상남도'),
]

class Clubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    leader_id = models.ForeignKey("accounts.Members", on_delete=models.CASCADE, related_name='leader')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    field = models.CharField(max_length=2, choices=FIELDS)
    location = models.CharField(max_length=2, choices=LOCATIIONS)
    age_group = models.CharField(max_length=20)
    limit = models.IntegerField()
    member = models.ManyToManyField(Members, related_name='member')
    image = models.CharField(max_length=100)


#? 용도를 잘 모르겠습니다.
class ClubMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id = models.ForeignKey("Clubs", on_delete=models.CASCADE)
    member_id = models.ForeignKey("accounts.Members", on_delete=models.CASCADE)


class Clubboard(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id= models.ForeignKey("Clubs", on_delete=models.CASCADE, db_column='club_id')
    writer_id= models.ForeignKey("accounts.Members", on_delete=models.CASCADE, db_column='writer_id')
    title = models.TextField()
    description = models.TextField()
    image = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    comment_cnt = models.IntegerField(default=0)


class Clubboard_comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer_id = models.ForeignKey("accounts.Members", on_delete=models.CASCADE)
    board_id = models.ForeignKey("Clubboard", on_delete=models.CASCADE)
    comment_id = models.ForeignKey("Clubboard_comment", on_delete=models.CASCADE)


class Galleries(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer_id = models.ForeignKey("accounts.Members", on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)