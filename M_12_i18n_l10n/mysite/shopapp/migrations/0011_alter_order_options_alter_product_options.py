# Generated by Django 4.0.6 on 2023-08-03 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0010_productimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
