# Generated by Django 4.0.5 on 2022-07-19 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(default='None', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderuname', models.CharField(default='', max_length=50)),
                ('recieveruname', models.CharField(default='', max_length=50)),
                ('content', models.CharField(default='', max_length=200)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Memories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memuname', models.CharField(default='', max_length=50)),
                ('text', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ybyear', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(default='', max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('branch', models.CharField(default='', max_length=20)),
                ('year', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='1920_1.jpg', upload_to='')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
