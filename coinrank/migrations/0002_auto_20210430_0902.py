# Generated by Django 3.1.6 on 2021-04-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinrank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinranking',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]