# Generated by Django 5.0.6 on 2024-06-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_birеhday_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Персонал'),
        ),
    ]