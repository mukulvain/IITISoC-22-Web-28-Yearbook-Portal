# Generated by Django 4.0.5 on 2022-07-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ybapp', '0004_remove_memories_student_memories_stuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='stuid',
            field=models.IntegerField(),
        ),
    ]
