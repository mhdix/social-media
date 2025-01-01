# Generated by Django 5.1.4 on 2024-12-31 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=20)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]
