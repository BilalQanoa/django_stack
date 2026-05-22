from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(32)])
    date = models.DateTimeField(auto_now_add=True)
