# Generated by Django 4.0.6 on 2023-08-04 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trendingproduct',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='trendingproduct',
            name='item_description',
        ),
        migrations.RemoveField(
            model_name='trendingproduct',
            name='price',
        ),
        migrations.RemoveField(
            model_name='trendingproduct',
            name='stock',
        ),
    ]
