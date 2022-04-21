from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, default='')
    name = models.TextField(null='True', default='')
    date = models.TextField(null='True', default='')
    date_str = models.CharField(max_length=20)
    date_int = models.DateField(default=timezone.now)
    time_start = models.TextField(null='True', default='')
    time_end = models.TextField(null='True', default='')
    active = models.TextField(null='True', default='')

    def __str__(self):
        return self.title

