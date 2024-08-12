# Generated by Django 5.0.6 on 2024-06-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=256, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Пользователь'),
        ),
    ]
