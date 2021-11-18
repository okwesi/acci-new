from django.db import models
import datetime

# Create your models here.
class Home(models.Model):
    header_image = models.ImageField(upload_to="media/home" )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=800)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
class Devotion(models.Model):
    header_image = models.ImageField(upload_to="media/devotion" )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=800)
    date = models.DateField(("Date"), default=datetime.date.today)
    
    def __str__(self):
        return self.title
    
    
    
class Branches(models.Model):
    header_image = models.ImageField(upload_to="media/branches" )
    pastors_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    telephone = models.IntegerField()
    
     
    
    def __str__(self):
        return self.pastors_name
    