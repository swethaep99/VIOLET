# Generated by Django 4.2.1 on 2023-06-05 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_category_cat_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='quantity',
        ),
    ]
