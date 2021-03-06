# Generated by Django 3.2.6 on 2021-08-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('menu_size', models.CharField(choices=[('v', 'Veg'), ('n', 'Non-Veg'), ('D', 'Drinks')], max_length=1)),
            ],
        ),
    ]
