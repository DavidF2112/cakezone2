# Generated by Django 5.1 on 2024-08-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_review_clients_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_clients',
            name='photo',
            field=models.ImageField(default=None, upload_to='staff_photos'),
        ),
    ]
