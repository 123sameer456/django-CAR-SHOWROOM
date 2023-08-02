from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class ShowRoom(models.Model):

    name = models.CharField(max_length=200 , default="unamed" , null=True)
    location = models.CharField(max_length=200 , default="not defined" , null=True)
    contact = models.CharField(max_length=200 , default="not defined" , null=True)
    email = models.EmailField(max_length=200 , unique = True , )
    capacity = models.IntegerField( null=True)

     
    def __str__(self):  
        return "%s" % (self.name)


    
class Staff(models.Model):
    image = models.ImageField(null = True , blank = True)
    first_name = models.CharField(max_length=200 , default="unamed" , null=True)
    last_name = models.CharField(max_length=200 , default="unamed" , null=True)
    designation = models.CharField(max_length=200 , default="unamed" , null=True)
    contact = models.CharField(max_length=200 , default="unamed" , null=True)
    email = models.EmailField(max_length=200 , unique = True)
    join_date = models.DateField()

    showroom_staff = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)  

    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)

class Brand(models.Model):
     brand_name = models.CharField(max_length=200 , default="unamed" , null=True)
     brand_image = models.ImageField(null = True , blank = True)

     def __str__(self):  
        return "%s" % (self.brand_name)

class Modell(models.Model):
    model_name = models.CharField(max_length=200 , default="unamed" , null=True)
    brand = models.CharField(max_length=200 , default="unamed" , null=True)
    year = models.IntegerField( null=True)
    price = models.DecimalField(max_digits=19, decimal_places=10 )

    brand_model = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    def __str__(self):  
        return "%s" % (self.model_name) 

class Engine(models.Model):
    engine_type = models.CharField(max_length=200 , default="unamed" , null=True)
    horse_power = models.IntegerField(null=True)
    fuel_type = models.CharField(max_length=200 , default="unamed" , null=True)

    engine_model = models.OneToOneField(Modell, on_delete=models.CASCADE)
    def __str__(self):  
        return "%s" % (self.engine_type)
class Feature(models.Model):
    feature_name = models.CharField(max_length=200 , default="unamed" , null=True)
    description = models.TextField()
    def __str__(self):  
        return "%s" % (self.feature_name)
