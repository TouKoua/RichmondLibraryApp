# Generated by Django 4.2.5 on 2023-11-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Richmond_Library_App', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=14),
        ),
    ]