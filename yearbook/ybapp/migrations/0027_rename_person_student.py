# Generated by Django 4.0.5 on 2022-07-13 17:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ybapp', '0026_delete_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Student',
        ),
    ]