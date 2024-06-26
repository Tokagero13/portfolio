# Generated by Django 5.0.2 on 2024-06-25 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us_msg', models.CharField(max_length=250, verbose_name='Contact Us message')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='cv.personalinfo', verbose_name='messages')),
            ],
        ),
    ]
