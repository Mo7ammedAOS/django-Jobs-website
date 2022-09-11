# Generated by Django 4.1.1 on 2022-09-11 18:33

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.uploaded_images),
            preserve_default=False,
        ),
    ]
