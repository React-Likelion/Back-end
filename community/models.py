from django.db import models
from accounts.models import User

CATEGORY = [
    ('공지','공지'),
    ('정보','정보'),
    ('자유','자유')
]

class Community(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="community/", null=True)
    create_time = models.DateTimeField('CREATE DT', auto_now_add=True)

    writer_nickname = models.ForeignKey(User, to_field='nickname', on_delete=models.CASCADE, related_name='community_writer')
    writer_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='community_writerid')

    category = models.CharField(max_length=10,choices=CATEGORY)
    comment_cnt = models.IntegerField(default=0) 

    class Meta:
        db_table = 'community'

    def __str__(self):
        return str(self.title)

class CommunityComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    create_time = models.DateTimeField('CREATE DT', auto_now_add=True)

    writer_nickname = models.ForeignKey(User, to_field='nickname', on_delete=models.CASCADE, related_name='comment_writer')
    writer_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comment_writerid')

    board_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='board')
    comment_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comment', null=True, blank=True)

    class Meta:
        db_table = 'communitycomments'

    def __str__(self):
        return str(self.content)