from django.db import models

# Create your models here.

class XSS(models.Model):
    cookies = models.TextField()
    referer = models.TextField()