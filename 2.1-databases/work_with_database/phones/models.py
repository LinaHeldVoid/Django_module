from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField
    price = models.CharField(max_length=20)
    release_date = models.DateField
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField(max_length=50)
    pass
