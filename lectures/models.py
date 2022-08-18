from accounts.models import User
from django.db import models

MAIN_CATEGORY = [
    ('미술', '미술'),
    ('요리', '요리'),
    ('음악', '음악'),
    ('운동', '운동'),
    ('외국어', '외국어'),
    ('사진/영상', '사진/영상'),
    ('창업/부업', '창업/부업'),
    ('프로그래밍', '프로그래밍'),
    ('금융/제테크', '금융/제테크'),
    ('라이프스타일', '라이프스타일'),
    ('비즈니스/마케팅', '비즈니스/마케팅'),
]

SUB_CATEGORY = [
    ('영어', '영어'),
    ('제2외국어', '제2외국어'),
    ('그림', '그림'),
    ('공예', '공예'),
    ('디자인', '디자인'),
    ('미술 기타', '기타'),
    ('요리', '요리'),
    ('베이킹', '베이킹'),
    ('음료/주류', '음료/주류'),
    ('요가/필라테스', '요가/필라테스'),
    ('헬스', '헬스'),
    ('운동 기타', '기타'),
    ('웹/앱', '웹/앱'),
    ('IT교양', 'IT교양'),
    ('법률', '법률'),
    ('상담', '상담'),
    ('뷰티', '뷰티'),
    ('라이프스타일 기타', '기타'),
    ('부동산', '부동산'),
    ('주식', '주식'),
    ('제테크', '제테크'),
    ('선택안함', '선택안함')
]

class Lectures(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    youtube_link = models.CharField(max_length=255)
    
    main_category = models.CharField(max_length=10,choices=MAIN_CATEGORY)
    sub_category = models.CharField(max_length=10,choices=SUB_CATEGORY)

    writer_nickname = models.ForeignKey(User, to_field='nickname', on_delete=models.CASCADE, related_name='writer')
   
    create_date = models.DateTimeField('CREATE DT', auto_now_add=True)

    enroll_students = models.ManyToManyField(User, symmetrical=False, through='EnrollStudents', through_fields=('lectures', 'user'), related_name='enroll_students', blank=True)
    enroll_cnt = models.IntegerField(default = 0)

    like_members = models.ManyToManyField(User, symmetrical=False, through='LikeMembers', through_fields=('lectures', 'user'), related_name='like_members', blank=True)
    like_cnt = models.IntegerField(default = 0)

    visit_cnt = models.IntegerField(default = 0)

    image1 = models.ImageField(upload_to="lectures/")
    image2 = models.ImageField(blank=True, upload_to="lectures/", null=True)
    image3 = models.ImageField(blank=True, upload_to="lectures/", null=True)
    image4 = models.ImageField(blank=True, upload_to="lectures/", null=True)
    image5 = models.ImageField(blank=True, upload_to="lectures/", null=True)
    

    class Meta:
        db_table = 'lectures'

    def __str__(self):
        return str(self.title)

#강의 수강
class EnrollStudents(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='nickname' ,on_delete=models.CASCADE, related_name='enroll_user')
    lectures = models.ForeignKey(Lectures, null=True , on_delete=models.CASCADE, related_name='enroll_lectures')
    
    class Meta:
        db_table = 'enroll'

#강의 좋아요
class LikeMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='nickname' ,on_delete=models.CASCADE, related_name='like_user')
    lectures = models.ForeignKey(Lectures, null=True , on_delete=models.CASCADE, related_name='like_lectures')

    class Meta:
        db_table = 'like'
