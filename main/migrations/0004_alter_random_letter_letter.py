# Generated by Django 4.2.5 on 2023-09-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_random_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='random_letter',
            name='letter',
            field=models.CharField(max_length=200),
        ),
    ]
