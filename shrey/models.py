from django.db import models

# Create your models here.

class student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    std=models.IntegerField()
    rno=models.IntegerField()
    image=models.ImageField(upload_to="uploads/",default="")
    
    def __str__(self):
        return self.fname
    
class product(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="uploads/",default="")
    
    def __str__(self):
        return self.name
                

        
    