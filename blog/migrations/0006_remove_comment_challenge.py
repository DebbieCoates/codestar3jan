# Generated by Django 4.2.17 on 2025-01-06 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]