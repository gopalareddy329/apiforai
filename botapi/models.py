from django.db import models

# Create your models here.
class ListofQuestions(models.Model):
    question=models.TextField()
    ans=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.question