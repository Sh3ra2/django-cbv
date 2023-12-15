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
    occupation = models.CharField(choices=O_C,max_length=50, default="Web developer")
    start_date = models.DateField(auto_now=False, auto_now_add=False, null= True)
    end_date = models.DateField( auto_now=False, auto_now_add=False, null= True, blank = True)

    def __str__(self) -> str:
        return f"{self.id}({self.name})"


class projectmodel(models.Model):
    name = models.CharField(max_length=50, null=True)
    dev = models.ForeignKey(employeemodel, on_delete=models.CASCADE)
    duration = models.DurationField(null=True)
    type = models.CharField(null=True, max_length= 50)
    client = models.CharField(null=True, max_length= 100)


class clientmodel(models.Model):
    name = models.CharField(max_length=100, null=True)
    project = models.ForeignKey(projectmodel, on_delete=models.CASCADE, null = True, blank =  True)
    address = models.CharField(max_length=50, null=True)
    payment = models.IntegerField( null=True)
    method = models.CharField(max_length=50, null=True)
    due = models.IntegerField( null=True)