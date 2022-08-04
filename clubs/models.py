from django.db import models
"""
from accounts.models import Members
fields..?
"""


class Clubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    leader_id = models.ForeignKey("Members", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    field = models.ForeignKey("Fields", on_delete=models.CASCADE)
    location = models.ForeignKey("Locations", on_delete=models.CASCADE)
    age_group = models.CharField(max_length=20)
    limit = models.IntegerField()
    member = models.ManyToManyField(Members)
    image = models.CharField()


class Clubmembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    club_id = models.ForeignKey("Clubs", on_delete=models.CASCADE)
    member_id = models.ForeignKey("Memebers", on_delete=models.CASCADE)


class Clubboard(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer_id = models.ForeignKey("Members", on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    image = models.CharField()
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20)
    comment_cnt = models.IntegerField()


class Clubboard_comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    writer_id = models.ForeignKey("Members", on_delete=models.CASCADE)
    board_id = modelds.ForeignKey("Clubboard", on_delete=models.CASCADE)
    comment_id = models.ForeignKey("Clubboard_comment", on_delete=models.CASCADE)


class Galleries(models.Model):
    id = models.BigAutoField(primary_key=True)
    writer_id = models.ForeignKey("Members", on_delete=CASCADE)
    title = models.CharField()
    image = models.CharField()
    upload_time = models.DateTimeField(auto_now_add=True)