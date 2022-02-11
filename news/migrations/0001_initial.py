# Generated by Django 4.0.2 on 2022-02-10 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
