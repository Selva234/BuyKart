# Generated by Django 5.2 on 2025-06-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
    ]
