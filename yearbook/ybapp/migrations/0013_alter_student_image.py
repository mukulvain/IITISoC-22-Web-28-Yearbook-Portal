# Generated by Django 4.0.5 on 2022-07-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0012_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='1920_1.jpg', upload_to=''),
        ),
    ]