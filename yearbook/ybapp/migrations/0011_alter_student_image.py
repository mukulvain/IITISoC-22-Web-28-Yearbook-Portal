# Generated by Django 4.0.5 on 2022-07-06 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0010_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='2.png', upload_to=''),
        ),
    ]