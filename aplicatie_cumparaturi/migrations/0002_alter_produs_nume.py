# Generated by Django 4.2.7 on 2024-03-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie_cumparaturi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produs',
            name='nume',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]