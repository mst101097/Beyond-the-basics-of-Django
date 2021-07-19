from django.db import models
from actors.models import Actor
# Create your models here.

class Movie(models.Model):
	title = models.CharField(max_length=200)
	actors = models.ManyToManyField(Actor,blank = True)
	date = models.DateTimeField(auto_now_add = True)


	class Meta:
		abstract = True

class Flim(Movie):
	length = models.CharField(max_length=200)

	def __str__(self):
		return self.title


class Commercial(Movie):
	company = models.CharField(max_length=120)


	def __str__(self):
		return self.company

