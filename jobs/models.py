from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(default="Kobe", max_length = 200)
	summary = models.TextField(null=True)
	link = models.URLField(max_length=128, blank=True)
	github= models.URLField(max_length=128, blank=True)