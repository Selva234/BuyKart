# Generated by Django 5.2 on 2025-06-24 22:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_amount_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Amount',
            new_name='OrderSummary',
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
