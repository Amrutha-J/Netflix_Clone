# Generated by Django 4.0.2 on 2022-02-27 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
