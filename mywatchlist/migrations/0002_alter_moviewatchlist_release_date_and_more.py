# Generated by Django 4.1 on 2022-09-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviewatchlist',
            name='release_date',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='moviewatchlist',
            name='title',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='moviewatchlist',
            name='watched',
            field=models.CharField(max_length=225),
        ),
    ]
