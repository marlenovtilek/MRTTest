# Generated by Django 5.0.6 on 2024-05-20 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('ADMIN', 'Администратор'), ('DOCTOR', 'Врач'), ('PATIENT', 'Пациент')], max_length=20, null=True, verbose_name='Позиция пользователя'),
        ),
    ]
