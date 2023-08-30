from django.db import models

# Create your models here.
class ErkaklarKiyimi(models.Model):
    name = models.CharField(max_length=100,default = ' shim ')
    colour = models.CharField(max_length=50,default = 'oq')

    def __str__(self) -> str:
        return self.name
class AyollarKiyimi(models.Model):
    name = models.CharField(max_length=100,default = 'yupka')
    colour = models.CharField(max_length=50,default = 'qora')
    price = models.IntegerField(default = 100000000)

    def __str__(self) -> str:
        return self.name
