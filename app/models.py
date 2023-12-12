from django.db import models

O_C = (
    ("web dev", "Web developer"),
    ("android dev", "Android developer"),
    ("ios dev", "IOS developer"),
)

# Create your models here.
class employeemodel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    occupation = models.CharField(choices=O_C,max_length=50)