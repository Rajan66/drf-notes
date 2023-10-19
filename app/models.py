from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100,null=True)
    body = models.TextField(null=False)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
