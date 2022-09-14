from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Porofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE,null=True,blank=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to ='profile/')

# create new user ----> create new profile using django signals

@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created,**kwrgs):
    if created:
        Porofile.objects.create(user = instance)



class City(models.Model):
    name = models.CharField(max_length=30)
