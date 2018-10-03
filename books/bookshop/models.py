from django.db import models
from decimal import Decimal
from django.urls import reverse
from datetime import datetime
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


VAT = (
    (0.23, " 23 % "),
    (0.08, " 8 % "),
    (0.05, " 5 % "),
    (0, " 0 % "),
)


class Author(models.Model):
    author_first_name = models.CharField(max_length=64)
    author_last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.author_last_name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Tytuł")
    slug = models.SlugField(max_length=200, blank=True, db_index=True)
    author = models.ManyToManyField(Author, blank=True, verbose_name="author")
    description = models.TextField(verbose_name="opis")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="cena")
    vat = models.FloatField(choices=VAT, verbose_name="Vat")
    stock = models.PositiveIntegerField(verbose_name="w magazynie")
    categories = models.ManyToManyField(Category, blank=True, verbose_name="kategorie")
    book_logo = models.FileField(max_length=1000, upload_to='products/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Comment(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    text = models.TextField()
    
    book = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    # reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')





class Image(models.Model):
    name = models.CharField(max_length=500, null=True)
    videofile = models.FileField(max_length=1000, upload_to='products/%Y/%m/%d', null=True)


    def __str__(self):
        return self.name
