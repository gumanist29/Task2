from django.db import models

# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=10)
	mainadress=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	category=models.CharField(max_length=20)
	contacts = models.IntegerField()
	branches=models.CharField(max_length=100)
	open=models.FloatField()
	close=models.FloatField()
	cost = models.IntegerField()


	def __str__(self):
		return self.name
