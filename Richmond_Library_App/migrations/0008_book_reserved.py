# Generated by Django 4.2.7 on 2023-11-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Richmond_Library_App', '0007_merge_20231102_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]