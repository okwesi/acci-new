# Generated by Django 3.2.6 on 2021-11-18 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acci_main', '0003_auto_20211118_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
