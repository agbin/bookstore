from django.contrib import admin
from .models import Product, Category, Author, Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'vat', 'stock', 'book_logo']

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_first_name', 'author_last_name']

@admin.register(Image)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'videofile']