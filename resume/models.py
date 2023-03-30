from django.db import models

# Create your models here.
class Skill(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Achievement(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    certificate=models.ImageField(upload_to='certificate',null=True)
    url=models.CharField(max_length=1000 ,null=True)

    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    project=models.ImageField(upload_to='project',null=True)
    url=models.CharField(max_length=1000 ,null=True)

    def __str__(self) -> str:
        return self.name
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    comment = models.TextField()

    def __str__(self):
        return "Query by "+self.name