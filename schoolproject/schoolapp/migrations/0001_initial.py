# Generated by Django 4.2.7 on 2023-11-28 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('st_num', models.CharField(max_length=200)),
                ('msg_num', models.IntegerField()),
            ],
        ),
    ]
