# Generated by Django 4.2.6 on 2023-10-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]