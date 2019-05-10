from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments') # 자기가 속한 댓글들을 보고 싶을 때 comments라는 이름으로 바로 부를 수 있다.
  comment = models.TextField(default=" ")