# Generated by Django 4.0.3 on 2022-04-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]