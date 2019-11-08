from django.db import models


class User(models.Model):
    class Meta:

        db_table = 'user'

    name = models.CharField(max_length=200)
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
