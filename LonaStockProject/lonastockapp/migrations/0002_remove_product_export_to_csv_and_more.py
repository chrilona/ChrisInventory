# Generated by Django 4.1.5 on 2023-02-02 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lonastockapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='product',
            name='issued_to',
        ),
    ]
