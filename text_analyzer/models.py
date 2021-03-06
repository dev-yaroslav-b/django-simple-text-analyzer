from django.db import models


class Post(models.Model):
    word = models.CharField(max_length=2000)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.word
