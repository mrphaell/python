from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=300)
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    birth = models.DateField()

    def __str__(self):
        return self.name
