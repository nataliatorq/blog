# Generated by Django 5.1 on 2024-08-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesse',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='interesses/'),
        ),
    ]
