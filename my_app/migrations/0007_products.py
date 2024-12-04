# Generated by Django 5.1.3 on 2024-12-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_rename_chair_cars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('original_price', models.CharField(max_length=30)),
                ('discounted_price', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
