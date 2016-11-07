from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
class blog_serverservice(models.Model):
    user = models.CharField(max_length=50)
    pid   = models.CharField(max_length=10)
    command = models.CharField(max_length=200)
    fileServer = models.CharField(max_length=200)
    class Meta:
        db_table = u'blog_serverservice'
'''
class student(models.Model):
    name = models.CharField(max_length=20)
    classes = models.CharField(max_length=50)
    age = models.CharField(max_length=10)

    class Meta:
        db_table = u'student'