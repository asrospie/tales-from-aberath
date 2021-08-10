# Generated by Django 3.2.6 on 2021-08-10 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='permalink',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]