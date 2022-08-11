from django.db import models

from accounts.models import User

JOB_CHOICES = [
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
    ('없음', '없음')
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
    ('경기도', '경기도'),
    ('강원도', '강원도'),
    ('충청북도', '충청북도'),
    ('충청남도', '충청남도'),
    ('전라북도', '전라북도'),
    ('전라남도', '전라남도'),
    ('경상북도', '경상북도'),
    ('경상남도', '경상남도'),
]

class Clubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    leader_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='leader')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    field = models.CharField(max_length=20, choices=JOB_CHOICES)
    location = models.CharField(max_length=20, choices=LOCATIIONS)
    age_group = models.CharField(max_length=20)
    limit = models.IntegerField()
    member = models.ManyToManyField(User, related_name='member')
    image = models.ImageField(blank=True, upload_to="clubs/", null=True)

    def member_cnt(self):
        return self.member.all().count()


#? 용도를 잘 모르겠습니다.
class ClubMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id = models.ForeignKey("Clubs", on_delete=models.CASCADE)
    member_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)


class Clubboard(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id= models.ForeignKey("Clubs", on_delete=models.CASCADE, db_column='club_id')
    writer_id= models.ForeignKey("accounts.User", on_delete=models.CASCADE, db_column='writer_id')
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="clubs/", null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    comment_cnt = models.IntegerField(default=0)


class Clubboard_comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    board_id = models.ForeignKey("Clubboard", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Galleries(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id= models.ForeignKey("Clubs", on_delete=models.CASCADE, db_column='club_id')
    writer_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE, db_column='writer_id')
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to="clubs/", null=True)
    upload_time = models.DateTimeField(auto_now_add=True)