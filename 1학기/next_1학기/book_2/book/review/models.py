from django.db import models

# after creating model, you have to inform the model to admin.py
# Create your models here.
class Review(models.Model):
  title = models.CharField(max_length = 200)
  description = models.TextField()
  price = models.IntegerField()
  SCORE_CHOICES = (
    ("별로 추천하지 않아요", "노잼"),
    ("입문자가 쉽게 볼 수 있는 책이에요", "순한 맛"),
    ("유익하지만 어려운 책이에요", "몸에 좋은 맛"),
    ("교과서 같이 자세히 공부할 수 있는 책이에요", "교과서"),
    ("선택하지 않음", "----"),
  )
  score = models.CharField(
    max_length = 200,
    default = "선택하지 않음",
    choices = SCORE_CHOICES
  )

  def __str__(self):
    return self.title

class Comment(models.Model):
  review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
  user = models.CharField(max_length = 200)
  content = models.TextField()