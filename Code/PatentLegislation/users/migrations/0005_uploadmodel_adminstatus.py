# Generated by Django 2.0.13 on 2021-02-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_uploadmodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmodel',
            name='adminstatus',
            field=models.CharField(default='waiting', max_length=600),
        ),
    ]
