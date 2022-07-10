from django.db import models


# Create your models here.
class cuisine(models.Model):
    typeid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20, blank=True)
    num = models.CharField(max_length=15, blank=True)


class Menu(models.Model):
    id = models.BigAutoField(primary_key=True)
    typeid = models.ForeignKey(cuisine, to_field='typeid', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=30)
    upload = models.ImageField(upload_to='static', blank=True)
    price = models.IntegerField()
    menu_types = (
        ('v', 'Veg'),
        ('n', 'Non-Veg'),
        ('s', 'Desserts'),
        ('D', 'Drinks'),
    )
    menu_size = models.CharField(max_length=1, choices=menu_types)
