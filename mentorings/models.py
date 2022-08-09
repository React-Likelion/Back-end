from django.db import models
from accounts.models import User
#usermodel 가져와서 manytomany로 만들어줌

class mentorings(models.Model):
    #locations에서 foreign키
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, db_column="user_id",null=True);
    nickname=models.CharField(max_length=255, null=True, blank=False)
    location=models.ForeignKey("locations",on_delete=models.CASCADE, db_column="location_id", null=True);
    #fields에서 foreign키
    field=models.CharField(max_length=255, null=True, blank=False);
    
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
    
    
class locations(models.Model):
    location=models.CharField(max_length=255, null=True, blank=False)
    
    def __str__(self):
        return self.location