# Generated by Django 2.1 on 2018-09-15 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='image_name',
        ),
    ]
