# Generated by Django 5.2 on 2025-06-25 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='delivery_charge',
        ),
        migrations.DeleteModel(
            name='Amount',
        ),
    ]
