from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Register(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	def __str__(self):
		return self.username

class Board(models.Model):
	subject = models.CharField(max_length=100)
	contents = models.TextField()
	writer = models.CharField(max_length=30)

	def __str__(self):
		return self.subject