from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    text = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
