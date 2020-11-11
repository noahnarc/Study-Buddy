# Generated by Django 3.1.2 on 2020-11-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0006_auto_20201103_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='studygroup',
            name='groupme_id',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studygroup',
            name='groupme_option',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studygroup',
            name='groupme_url',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]