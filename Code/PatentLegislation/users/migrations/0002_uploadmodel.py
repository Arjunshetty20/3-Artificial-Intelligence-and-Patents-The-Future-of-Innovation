# Generated by Django 2.2.3 on 2020-07-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('file', models.FileField(upload_to='files/pdfs/')),
            ],
            options={
                'db_table': 'Uploadfile',
            },
        ),
    ]
