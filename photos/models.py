# Create your models here.
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    bio = models.CharField(max_length =30)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 30,null = True)
    caption = models.TextField(null = True)
    user = models.ForeignKey(User,null=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
    	return self.name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image
    
    def __str__(self):
    	return self.user.username

    
    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos

class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField() 
class Comment(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,null = True)
    image = models.ForeignKey(Image,related_name='comment')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def find_commentimage(cls,id):
        comments = Comments.objects.filter(image__pk = id)
        return comments    