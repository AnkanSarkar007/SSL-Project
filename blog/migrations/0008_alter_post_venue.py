# Generated by Django 4.1.2 on 2022-11-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='venue',
            field=models.CharField(choices=[], max_length=100),
        ),
    ]
