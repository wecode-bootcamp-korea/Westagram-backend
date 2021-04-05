from django.db import models

class User(models.Model):
    email         = models.CharField(max_length=100)
    password      = models.CharField(max_length=100)
    name          = models.CharField(max_length=45)
    phone_number  = models.CharField(max_length=14)


    class Meta:
        db_table = 'users'


