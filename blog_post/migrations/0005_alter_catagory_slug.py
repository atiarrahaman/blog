# Generated by Django 5.0.1 on 2024-01-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
