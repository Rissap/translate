from django.db import models


class Numbers(models.Model):
	"""
	database table for roman-arabic numbers
	"""
	roman = models.CharField(max_length=5)
	arabic = models.IntegerField()

	def __str__(self):
		return "{0} {1}".format(self.roman, self.arabic)