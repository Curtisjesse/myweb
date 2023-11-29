from django.db import models

# Create your models here.
class Furniture(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'images')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=150)
    auther = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='blogs')
    
    def __str__(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=80, blank=False)
    image = models.FileField(upload_to='services')
    description = models.TextField(max_length=250, blank=False)
    
    def __str__(self):
        return self.title
    
class Teams(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250, blank=False)
    img = models.ImageField(upload_to='Teams')
    
    def __str__(self):
        return self.name
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=250, blank=False)
    img = models.ImageField(upload_to='Testimonials')
    
    def __str__(self):
        return self.name