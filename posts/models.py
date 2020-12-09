from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    image=models.ImageField(upload_to='images/')
    caption=models.TextField()

    def __str__(self):
        return self.caption[:15]

    def get_absolute_url(self):
        return reverse("postDetail",args=[str(self.id)])