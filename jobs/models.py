from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length = 200)
	link = models.URLField(max_length=128, blank=True)
	github= models.URLField(max_length=128, blank=True)