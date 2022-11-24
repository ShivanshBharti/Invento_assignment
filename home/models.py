from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Coder(models.Model):
    name= models.CharField(max_length=100)
    language = models.ManyToManyField(Language)
    
    def __str__(self):
        return self.name