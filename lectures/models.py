from distutils.command.upload import upload
from accounts.models import User
from django.db import models

# lectures main_category choice field
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

# lectures sub_category choice field
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

# lectures table 생성
class Lectures(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    youtube_link = models.CharField(max_length=255)
    
    # 카테고리
    main_category = models.CharField(max_length=10,choices=MAIN_CATEGORY)
    sub_category = models.CharField(max_length=10,choices=SUB_CATEGORY)

    writer_nickname = models.ForeignKey(User, to_field='nickname', on_delete=models.CASCADE, related_name='writer')
   
    create_date = models.DateTimeField('CREATE DT', auto_now_add=True)

    # 강의 수강 멤버 및 수 
    enroll_students = models.ManyToManyField(User, symmetrical=False, through='EnrollStudents', through_fields=('lectures', 'user'), related_name='enroll_students', blank=True)
    enroll_cnt = models.IntegerField(default = 0)

    # 강의 좋아요 멤버 및 수 
    like_members = models.ManyToManyField(User, symmetrical=False, through='LikeMembers', through_fields=('lectures', 'user'), related_name='like_members', blank=True)
    like_cnt = models.IntegerField(default = 0)

    # 강의 조회수
    visit_cnt = models.IntegerField(default = 0)
    
    thumbnail=models.ImageField(upload_to="lectures/")
    
    class Meta:
        db_table = 'lectures'

    def __str__(self):
        return str(self.title)
    

#이미지 테이블 생성
class Lecture_Image(models.Model):
    lecture=models.ForeignKey(Lectures, on_delete=models.CASCADE, related_name='lectures_image')
    image=models.ImageField(blank=True, upload_to="lectures/", null=True)

# 강의 수강
class EnrollStudents(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='nickname' ,on_delete=models.CASCADE, related_name='enroll_user')
    lectures = models.ForeignKey(Lectures, null=True , on_delete=models.CASCADE, related_name='enroll_lectures')
    
    class Meta:
        db_table = 'enroll'

# 강의 좋아요
class LikeMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, to_field='nickname' ,on_delete=models.CASCADE, related_name='like_user')
    lectures = models.ForeignKey(Lectures, null=True , on_delete=models.CASCADE, related_name='like_lectures')

    class Meta:
        db_table = 'like'
