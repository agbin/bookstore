# Generated by Django 2.1 on 2018-10-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0007_comment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default=(1, 0), max_length=200),
            preserve_default=False,
        ),
    ]