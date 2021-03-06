# Generated by Django 2.1 on 2018-09-03 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(max_length=64)),
                ('author_last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Tytuł')),
                ('description', models.TextField(verbose_name='opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='cena')),
                ('vat', models.FloatField(choices=[(0.23, ' 23 % '), (0.08, ' 8 % '), (0.05, ' 5 % '), (0, ' 0 % ')], verbose_name='Vat')),
                ('stock', models.PositiveIntegerField(verbose_name='w magazynie')),
                ('book_logo', models.FileField(max_length=1000, upload_to='.')),
                ('author', models.ManyToManyField(blank=True, to='bookshop.Author', verbose_name='author')),
                ('categories', models.ManyToManyField(blank=True, to='bookshop.Category', verbose_name='kategorie')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookshop.Product'),
        ),
    ]
