from django.db import models
from accounts.models import User
#usermodel 가져와서 manytomany로 만들어줌
from clubs.models import LOCATIIONS, JOB_CHOICES

class mentorings(models.Model):
    #locations에서 foreign키
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id", null=True);
    nickname=models.CharField(max_length=255,null=True)
    location = models.CharField(max_length=20, choices=LOCATIIONS)
    #fields에서 foreign키
    field=models.CharField(max_length=20, choices=JOB_CHOICES);
    
    title=models.TextField();
    description=models.TextField();

    age_group=models.IntegerField();
    limit=models.IntegerField();
    tag=models.CharField(max_length=255);
    image = models.ImageField(upload_to="%Y/%m/%d")
    create_date=models.DateTimeField(auto_now_add=True);
    #member와 ManytoMany연결
    User=models.ManyToManyField(User, through='mentoringsTouser', related_name='Member');
    member_cnt=models.IntegerField(default=0);
    
class mentoringsTouser(models.Model):
    user=models.ForeignKey(User,related_name='mentoringsTouser',on_delete=models.CASCADE)
    mentorings=models.ForeignKey('mentorings',related_name='mentoringsTouser',on_delete=models.CASCADE)


    
class mentoring_chats(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id",null=True, blank=True);
    nickname=models.CharField(max_length=255,null=True, blank=True)
    description=models.TextField();
    create_date=models.DateTimeField(auto_now_add=True);
    mentorings_id=models.ForeignKey("mentorings", on_delete=models.CASCADE, db_column="mentorings_id")

