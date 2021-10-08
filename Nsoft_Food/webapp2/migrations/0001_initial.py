# Generated by Django 3.2.5 on 2021-09-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cu_img', models.FileField(upload_to='cuisine/')),
                ('cu_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_cost', models.FloatField()),
                ('item_image', models.ImageField(upload_to='page_items_image/')),
                ('item_logo', models.ImageField(upload_to='page_items_logo/')),
                ('logo_desc', models.CharField(max_length=100)),
                ('item_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page_Nav_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_pic', models.FileField(upload_to='page_nav/')),
                ('item_text', models.CharField(max_length=100)),
            ],
        ),
    ]
