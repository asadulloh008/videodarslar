# Generated by Django 5.0.1 on 2024-03-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_alter_video_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default=1, upload_to='video/images'),
            preserve_default=False,
        ),
    ]
