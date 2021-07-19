from django.db import models

# Create your models here.

class Actor(models.Model):
	name = models.CharField(max_length=20)
	is_star = models.BooleanField(default = False)


	def __str__(self):
		return str(self.name)

