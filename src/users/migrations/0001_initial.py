# Generated by Django 3.1.5 on 2021-01-25 21:36

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTayBxqNcpOECgVloLid0g8WYj7qn6w7k-dhQ&usqp=CAU', max_length=5000)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
