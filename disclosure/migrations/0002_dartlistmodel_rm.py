# Generated by Django 3.2.5 on 2022-02-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disclosure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dartlistmodel',
            name='rm',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
