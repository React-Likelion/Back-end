from django.db import models

JOB_CHOICES = [
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

class Members(models.Model):
    id = models.BigAutoField(primary_key=True)
    identification = models.CharField(max_length=11)
    name = models.CharField(max_length=11)
    nickname = models.CharField(unique=True, max_length=11)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    birth = models.DateField(auto_now_add=False)
    job = models.CharField(max_length=2, choices=JOB_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.nickname)



