from django.db import models
import random

def generate_id():
  return str(random.randint(100000, 999999999))

# Create your models here.
class User(models.Model):
  email = models.EmailField(max_length=254)
  password = models.CharField(max_length=50)
  slug = models.CharField(max_length=10, default=generate_id)
  
  def __str__(self):
      return self.email