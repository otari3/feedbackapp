from django.db import models
import uuid

# Create your models here.

class Company(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.TextField(unique =True,null=False, blank=False)
  name = models.TextField(unique =True)
  
class Employee(models.Model):
  class Status(models.TextChoices):
    ADMIN = 'AD',('Admin')
    STANDARD ='SD',('standard')
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.TextField(unique =True,null=False, blank=False)
  name = models.TextField()
  tab = models.TextField()
  status = models.CharField( max_length=2,choices=Status.choices,default=Status.STANDARD)
  company = models.ForeignKey(Company,on_delete=models.CASCADE)