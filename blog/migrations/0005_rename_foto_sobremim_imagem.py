# Generated by Django 5.1 on 2024-08-29 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_sobremim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sobremim',
            old_name='foto',
            new_name='imagem',
        ),
    ]
