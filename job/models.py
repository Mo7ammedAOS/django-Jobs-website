from distutils import extension
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

def uploaded_images(instance,filename):
    imagename , extension = filename.split(".")
    return "job/%s.%s"%(instance.id,extension)

class Job(models.Model):
    JOB_TYPE =(
        ('Full Time','Full Time'),
        ('Part Time','Part Time')
    )
    owner = models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to =uploaded_images)
    slug = models.SlugField(blank=True,null=True)


    def save(self,*args,**kwrgs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwrgs)

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Job_Aplication(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='applications/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
