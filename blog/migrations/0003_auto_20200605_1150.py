# Generated by Django 3.0.6 on 2020-06-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
