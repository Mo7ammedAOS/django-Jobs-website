from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.email