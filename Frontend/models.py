import email
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    psw = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    
    class Meta:
        db_table = "user"
