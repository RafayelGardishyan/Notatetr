from django.db import models
import random

def generate_id():
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Create your models here.
class User(models.Model):
  email = models.EmailField(max_length=254)
  password = models.CharField(max_length=50)
  slug = models.CharField(default=generate_id)