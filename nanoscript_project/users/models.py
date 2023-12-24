from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    registrationDate  =  models.DateField("Registration Date", auto_now_add=True)
	
    def __str__(self):
        return self.first_name