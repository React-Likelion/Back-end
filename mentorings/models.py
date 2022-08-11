from django.db import models
from accounts.models import User
#usermodel 가져와서 manytomany로 만들어줌

FIELDS = [
    ('관리자', '관리자'),
    ('전문가 및 관련 종사자', '전문가 및 관련 종사자'),
    ('사무 종사자', '사무 종사자'),
    ('서비스 종사자', '서비스 종사자'),
    ('판매 종사자', '판매 종사자'),
    ('농림 어업 숙련 종사자', '농림 어업 숙련 종사자'),
    ('기은원 및 관련 기능 종사자', '기은원 및 관련 기능 종사자'),
    ('장치 기계 조작 및 조립 종사자', '장치 기계 조작 및 조립 종사자'),
    ('단순 노무 종사자', '단순 노무 종사자'),
    ('군인 및 학생', '군인 및 학생'),
]

LOCATIIONS = [
    ('경기도', '경기도'),
    ('강원도', '강원도'),
    ('충청북도', '충청북도'),
    ('충청남도', '충청남도'),
    ('전라북도', '전라북도'),
    ('전라남도', '전라남도'),
    ('경상북도', '경상북도'),
    ('경상남도', '경상남도'),
]

class mentorings(models.Model):
    #locations에서 foreign키
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id",null=True);
    nickname=models.CharField(max_length=255, null=True, blank=False)
    location = models.CharField(max_length=20, choices=LOCATIIONS)
    #fields에서 foreign키
    field=models.CharField(max_length=20, choices=FIELDS, null=True, blank=False);
    
    title=models.TextField(null=True, blank=False);
    description=models.TextField(null=True, blank=False);

    age_group=models.IntegerField(null=True, blank=False);
    limit=models.IntegerField(default=0,null=True, blank=False);
    tag=models.CharField(max_length=255, null=True, blank=False);
    image = models.ImageField(upload_to="%Y/%m/%d")
    create_date=models.DateTimeField(auto_now_add=True);
    #member와 ManytoMany연결
    User=models.ManyToManyField(User, through='mentoringsTouser', related_name='Member');
    member_cnt=models.IntegerField(default=0, null=True, blank=False);
    
class mentoringsTouser(models.Model):
    user=models.ForeignKey(User,related_name='mentoringsTouser',on_delete=models.CASCADE, null=True)
    mentorings=models.ForeignKey('mentorings',related_name='mentoringsTouser',on_delete=models.CASCADE, null=True)


    
class mentoring_chats(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id",null=True);
    nickname=models.CharField(max_length=255, null=True, blank=False)
    description=models.TextField(null=True, blank=False);
    create_date=models.DateTimeField(auto_now_add=True);
    mentorings_id=models.ForeignKey("mentorings", on_delete=models.CASCADE, db_column="mentorings_id")

