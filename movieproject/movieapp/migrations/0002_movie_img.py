# Generated by Django 5.0 on 2024-03-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ddffdfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
