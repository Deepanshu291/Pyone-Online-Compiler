# Generated by Django 4.0.2 on 2022-12-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0002_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.TextField(),
        ),
    ]
