from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)  # Unique constraint for usernames
    email = models.EmailField(max_length=40, unique=True)   # Use EmailField for validation
    password = models.CharField(max_length=128)            # Increased length for hashed passwords
