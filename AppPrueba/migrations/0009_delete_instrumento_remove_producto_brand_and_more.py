# Generated by Django 5.0.6 on 2024-06-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPrueba', '0008_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Instrumento',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='price',
        ),
        migrations.AlterField(
            model_name='producto',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]