# Generated by Django 3.2.9 on 2021-11-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_author_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fullName',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
