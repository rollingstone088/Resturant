# Generated by Django 3.2.6 on 2021-09-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cuisine_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_size',
            field=models.CharField(choices=[('v', 'Veg'), ('n', 'Non-Veg'), ('s', 'Desserts'), ('D', 'Drinks')], max_length=1),
        ),
    ]
