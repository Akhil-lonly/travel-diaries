# Generated by Django 4.1 on 2022-09-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_rename_tplace_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=250)),
                ('img2', models.ImageField(upload_to='pics')),
                ('dis2', models.TextField()),
            ],
        ),
    ]