# Generated by Django 5.0.2 on 2024-06-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='contact_us_msg',
            field=models.TextField(max_length=250, verbose_name='Contact Us message'),
        ),
    ]