# Generated by Django 3.2.9 on 2022-01-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220128_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hot',
            field=models.BooleanField(default=False),
        ),
    ]
