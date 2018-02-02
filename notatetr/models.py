from django.db import models
import random

def generate_id():
  return str(random.randint(100000, 999999999))

# Create your models here.
class User(models.Model):
  email = models.EmailField(max_length=254, unique=True)
  password = models.CharField(max_length=50)
  slug = models.CharField(max_length=10, default=generate_id)

  def __str__(self):
      return self.slug

class Note(models.Model):
    content = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    slug = models.CharField(max_length=100, default=generate_id)

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)