# Generated by Django 3.1.4 on 2021-01-26 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_books_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='price',
        ),
    ]
