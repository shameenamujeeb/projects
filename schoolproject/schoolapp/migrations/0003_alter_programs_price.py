# Generated by Django 4.2.7 on 2023-11-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_programs_delete_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programs',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
