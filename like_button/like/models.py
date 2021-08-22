from django.db import models
from django.contrib.auth.models import User

class LikeButton(models.Model):
    content=models.TextField(null=True)
    likes=models.IntegerField(default=0)

    @property
    def total_likes(self):
        return self.likes
