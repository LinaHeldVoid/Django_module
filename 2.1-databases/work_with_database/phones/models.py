from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    image = models.CharField(max_length=300, null=False)
    price = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField(max_length=50)
