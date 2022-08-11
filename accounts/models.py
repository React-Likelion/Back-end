from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, identification, name, nickname, password, email, birth, job):

        if not identification:
            raise ValueError('must have member identification')
        if not name:
            raise ValueError('must have member name')
        if not nickname:
            raise ValueError('must have member nickname')
        if not email:
            raise ValueError('must have member email')
        if not birth:
            raise ValueError('must have member birth')
        if not job:
            raise ValueError('must have member job')

        User = self.model(
            identification = identification,
            name = name,
            nickname = nickname,
            email = self.normalize_email(email),
            birth = birth,
            job = job,
            
            is_active = True,
            is_admin = False,
            is_superuser = False,
        )
        User.set_password(password)
        User.save(using=self._db)
        return User
        
    # 관리자 user 생성
    def create_superuser(self, identification, name, nickname, password, email, birth, job, ):

        User = self.model(
            identification = identification,
            name = name,
            nickname = nickname,
            password = password, 
            email = self.normalize_email(email),
            birth = birth,
            job = job,

            is_active = False,
            is_staff = False,
            is_superuser = False,
        )
        User.set_password(password)
        User.save(using=self._db)

        return User
        
    # 관리자 user 생성
    def create_superuser(self, identification, name, nickname, password, email, birth, job):

        User = self.create_user(
            identification = identification,
            name = name,
            nickname = nickname,
            password = password, 
            email = self.normalize_email(email),
            birth = birth,
            job = job,
        )

        User.is_admin = True,
        User.is_superuser = True,
        User.is_active = True
        User.is_staff = True,
        User.save(using=self._db)        

        return User


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

class User(AbstractBaseUser):
    identification = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=11)
    nickname = models.CharField(unique=True, max_length=11)
    email = models.EmailField(max_length=254, unique=True)
    birth = models.DateField(auto_now_add=False)
    job = models.CharField(max_length=2, choices=JOB_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True) 

    #point
    point = models.IntegerField(default=10000)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 identification으로 설정
    USERNAME_FIELD = 'identification'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name', 'nickname', 'password', 'email', 'birth', 'job']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module(self, app_label):
        return True

    def __str__(self):
        return str(self.nickname)
        
    class Meta: #모든 모델에 class Meta 넣기
        db_table="User"

