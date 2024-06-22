# Generated by Django 5.0.2 on 2024-06-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_git_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git_url',
            field=models.URLField(blank=True, null=True, verbose_name='URL address (git, leetcode...)'),
        ),
    ]