# Generated by Django 4.1.1 on 2022-09-13 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_aplication_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_aplication',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
