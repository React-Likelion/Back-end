from django.db import models
#usermodel 가져와서 manytomany로 만들어줌

class mentorings(models.Model):
    #locations에서 foreign키
    location=models.CharField(max_length=255, null=True, blank=False);
    #fields에서 foreign키
    field=models.CharField(max_length=255, null=True, blank=False);
    
    title=models.TextField();
    description=models.TextField();

    age_group=models.IntegerField();
    limit=models.IntegerField();
    tag=models.CharField(max_length=255, null=True, blank=False);
    image=models.CharField(max_length=255, null=True, blank=False);
    
    #member와 ManytoMany연결
    member=models.CharField(max_length=255, null=True, blank=False);
    member_cnt=models.IntegerField();
    
class mentoring_chats(models.Model):
    description=models.TextField();
    create_date=models.DateTimeField();
    mentorings_id=models.ForeignKey("mentorings", on_delete=models.CASCADE, db_column="mentorings_id")