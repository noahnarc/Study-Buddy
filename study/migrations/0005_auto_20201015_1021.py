# Generated by Django 3.1.2 on 2020-10-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_auto_20201013_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='grad_year',
            field=models.CharField(blank=True, choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024')], max_length=30, verbose_name='Graduation Year'),
        ),
    ]
