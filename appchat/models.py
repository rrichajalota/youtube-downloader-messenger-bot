from __future__ import unicode_literals

from django.db import models

# Create your models here.
class QueryResults(models.Model):
	sno = models.IntegerField()
	text= models.CharField(max_length= 600) 
