# Generated by Django 4.2.16 on 2024-11-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_contactprofile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactprofile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
