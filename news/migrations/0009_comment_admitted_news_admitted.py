# Generated by Django 4.0.2 on 2022-02-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='admitted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='admitted',
            field=models.BooleanField(default=False),
        ),
    ]
