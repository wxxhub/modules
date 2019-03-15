from django.db import models

# class Article(models.Model):
#     title = models.CharField(max_length=32)
#     date = models.DateField(auto_now_add=True)
#     text = models.TextField()

# Create your models here.
class ChatData(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=256)

class User(models.Model):
    name = models.CharField(max_length=16)
    chat_data = models.ForeignKey(ChatData, on_delete=models.CASCADE)
