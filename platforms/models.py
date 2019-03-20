from django.db import models

# Create your models here.


class platforms(models.Model):
    Pid = models.CharField(max_length=50)
    type  = models.CharField(max_length=50)
