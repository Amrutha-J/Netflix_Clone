# Generated by Django 4.1.2 on 2022-11-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0002_alter_movie_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='file',
            field=models.FileField(upload_to='movies/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='preview_image',
            field=models.ImageField(upload_to='preview_images/'),
        ),
    ]
