from django.db import models 

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	biography = models.TextField()    #paragraphs, larger space

	def __str__(self):
		return self.first_name + " " + self.last_name #displayed in admin tab

		

class Sign(models.Model):
	astrology_sign = models.CharField(max_length=30)
	astrology_decan = models.CharField(max_length=30)
	birth_month = models.CharField(max_length=30)
	details = models.ForeignKey(Person)

	def __str__(self):
		return self.astrology_sign







