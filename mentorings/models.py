from django.db import models
#usermodel 가져와서 manytomany로 만들어줌

class mentorings(models.Model):
    #locations에서 foreign키
    location=models.ForeignKey("locations",on_delete=models.CASCADE, db_column="location_id");
    #fields에서 foreign키
    field=models.CharField(max_length=255, null=True, blank=False);
    
    title=models.TextField(null=True, blank=False);
    description=models.TextField(null=True, blank=False);

    age_group=models.IntegerField(null=True, blank=False);
    limit=models.IntegerField(null=True, blank=False);
    tag=models.CharField(max_length=255, null=True, blank=False);
    image=models.CharField(max_length=255, null=True, blank=False);
    
    #member와 ManytoMany연결
    member=models.CharField(max_length=255, null=True, blank=False);
    member_cnt=models.IntegerField(null=True, blank=False);
    
class mentoring_chats(models.Model):
    description=models.TextField(null=True, blank=False);
    create_date=models.DateTimeField(auto_now_add=True);
    mentorings_id=models.ForeignKey("mentorings", on_delete=models.CASCADE, db_column="mentorings_id")
    
    
class locations(models.Model):
    location=models.CharField(max_length=255, null=True, blank=False)
    
    def __str__(self):
        return self.location