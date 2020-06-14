from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField( max_length=100)
    about = models.TextField( max_length=300)
    img = models.ImageField(upload_to ='media/images')

    def __str__(self):
        return self.title 

class Client(models.Model):
    title = models.CharField( max_length=100)
    project_name = models.TextField(max_length=300)
    img = models.ImageField(upload_to ='media/images')
    url = models.URLField()

    def __str__(self):
        return self.title 

class Service(models.Model):
    title = models.CharField( max_length=100,)
    service_name = models.TextField(max_length=300)

    def __str__(self):
        return self.title 

class Message(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField( blank=False)
    message = models.TextField( blank=False)

    def __str__(self):
        return self.name
