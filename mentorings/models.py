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

CATEGORY = [
    ('외국어', '외국어'),
    ('미술', '미술'),
    ('요가/필라테스', '요가/필라테스'),
    ('헬스', '헬스'),
    ('법률', '법률'),
    ('상담', '상담'),
    ('뷰티', '뷰티'),
    ('프로그래밍', '프로그래밍'),
    ('비즈니스/마케팅', '비즈니스/마케팅'),
    ('사진/영상', '사진/영상'),
    ('부동산', '부동산'),
    ('주식', '주식'),
    ('재테크', '재테크'),
    ('창업/부업', '창업/부업'),
]


LOCATIIONS = [
    ('서울특별시', '서울특별시'),
    ('부산광역시', '부산광역시'),
    ('대구광역시', '대구광역시'),
    ('인천광역시', '인천광역시'),
    ('광주광역시', '광주광역시'),
    ('대전광역시', '대전광역시'),
    ('울산광역시', '울산광역시'),
    ('세종특별자치시', '세종특별자치시'), 
    ('경기도', '경기도'),
    ('강원도', '강원도'),
    ('충청북도', '충청북도'),
    ('충청남도', '충청남도'),
    ('전라북도', '전라북도'),
    ('전라남도', '전라남도'),
    ('경상북도', '경상북도'),
    ('경상남도', '경상남도'),
    ('제주특별자치도', '제주특별자치도')
]

class mentorings(models.Model):
    #locations에서 foreign키
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id",null=True);
    nickname=models.CharField(max_length=255, null=True, blank=False)
    location = models.CharField(max_length=20, choices=LOCATIIONS)
    #fields에서 foreign키
    field=models.CharField(max_length=20, choices=CATEGORY, null=True, blank=False);
    
    title=models.TextField(null=True, blank=False);
    description=models.TextField(null=True, blank=False);

    age_group=models.CharField(max_length=255, null=True, blank=False);
    limit=models.IntegerField(default=0,null=True, blank=False);
    tag=models.CharField(max_length=255, null=True, blank=False);
    tag2=models.CharField(max_length=255, null=True, blank=False);
    tag3=models.CharField(max_length=255, null=True, blank=False);
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

