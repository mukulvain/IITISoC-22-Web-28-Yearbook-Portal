# Generated by Django 4.0.5 on 2022-07-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0018_alter_student_fname_alter_student_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
    ]