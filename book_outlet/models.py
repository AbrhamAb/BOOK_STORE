from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    author = models.CharField(max_length=100)
    is_best_seller = models.BooleanField(default=False)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.title
