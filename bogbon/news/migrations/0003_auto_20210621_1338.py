# Generated by Django 3.1.4 on 2021-06-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]
