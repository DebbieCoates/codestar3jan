# Generated by Django 4.2.17 on 2025-01-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
