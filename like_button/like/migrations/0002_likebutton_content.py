# Generated by Django 3.0.8 on 2020-08-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likebutton',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
