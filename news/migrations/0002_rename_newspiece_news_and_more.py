# Generated by Django 4.0.2 on 2022-02-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsPiece',
            new_name='News',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='creation_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='published_date',
            new_name='pub_date',
        ),
    ]
