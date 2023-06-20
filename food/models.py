from django.db import models

# Create your models here.
from django.urls import reverse


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://www.jennycancook.com/wp-content/uploads/2014/08/comingsoon-480x300.jpg')

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:index")