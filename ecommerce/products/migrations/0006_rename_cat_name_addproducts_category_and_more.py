# Generated by Django 5.0.6 on 2024-06-27 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_category_addproducts_cat_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addproducts',
            old_name='cat_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat_name',
            new_name='category',
        ),
    ]
