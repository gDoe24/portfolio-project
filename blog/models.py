from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):

	title = models.CharField(max_length = 30)
	date = models.DateTimeField(default = datetime.today)
	author = models.CharField(max_length=30, null=True)
	body = models.TextField()
	image = models.ImageField(upload_to = 'images/')

	class Meta:
		ordering = ['-date',]

	def __str__(self):
		return self.title

	def summary(self):

		return self.body[:100]

	def pub_date(self):

		return self.date.strftime('%b %e, %Y')

class Comment(models.Model):

	post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
	username = models.CharField(max_length=30)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)


	def approved(self):
		self.approved=True
		self.save()


	def __str__(self):
		return self.username
