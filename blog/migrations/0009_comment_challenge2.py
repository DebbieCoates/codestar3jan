# Generated by Django 4.2.17 on 2025-01-06 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
