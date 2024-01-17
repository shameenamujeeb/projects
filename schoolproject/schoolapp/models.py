from django.db import models


# Create your models here.

class Programs(models.Model):
    price = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    less_time = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    desc = models.TextField()
    st_num = models.CharField(max_length=200)
    msg_num = models.IntegerField()
    def __str__(self):
        return self.name
