# Generated by Django 3.1.2 on 2020-11-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0005_auto_20201015_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='group_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
