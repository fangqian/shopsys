from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
         title = models.CharField(max_length=100)
         description = models.TextField()
         image_url = models.CharField(max_length=200)
         price = models.DecimalField(max_digits=8,decimal_places=2)