from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    rate=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.type
    
class Sales(models.Model):
    date=models.DateField()
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    price=models.IntegerField()


    