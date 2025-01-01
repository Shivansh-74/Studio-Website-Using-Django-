from django.db import models

# Create your models here.

class Home(models.Model):
    homeImages = models.ImageField(upload_to='homeImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    

class About(models.Model):
    aboutImages = models.ImageField(upload_to='aboutImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)
    
    
class Gallery(models.Model):
    galleryImages = models.ImageField(upload_to='galleryImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)   
    
class Wedding(models.Model):
    weddingImages = models.ImageField(upload_to='galleryImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)
    
    
class Birthday(models.Model):
    birthdayImages = models.ImageField(upload_to='galleryImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)
    
    
class Haldi(models.Model):
    haldiImages = models.ImageField(upload_to='galleryImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)
    
    
class Party(models.Model):
    partyImages = models.ImageField(upload_to='galleryImages')
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.date)
         
    
class Blog(models.Model):
    blogImages = models.ImageField(upload_to='blogImages')
    dateShow = models.CharField(max_length=100,null=True)
    discription = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.date)   
    
class Events(models.Model):
    package = models.CharField(max_length=100)
    eventImage = models.ImageField(upload_to='events')
    desc = models.CharField(max_length=300)
    time = models.CharField(max_length=200)    
    outfit = models.CharField(max_length=200)
    imageNum = models.IntegerField(default=90)
    graphy = models.CharField(max_length=200)
    price = models.IntegerField(default=1200)
    
    def __str__(self):
        return self.desc


class ContactForm(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    phone = models.IntegerField(null=True)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.name    
    
class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)    