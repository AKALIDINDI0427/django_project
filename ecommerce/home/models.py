from django.db import models

# Create your models here.


class HomeDetails(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    class Meta:
        db_table="HomeDetails"

