# Generated by Django 4.2.7 on 2023-12-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, height_field=200, upload_to='category', width_field=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='product', width_field=200),
        ),
    ]
