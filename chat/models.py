from django.db import models

# Create your models here.

class Chat(models.Model):
  question = models.TextField(max_length=500)
  answer = models.TextField(max_length=500)

  def __str__(self):
    return f"Q-{self.question[:50]}"