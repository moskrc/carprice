# Generated by Django 3.0.5 on 2020-04-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200324_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car',
        ),
        migrations.AddField(
            model_name='order',
            name='brand',
            field=models.CharField(blank=True, max_length=255, verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.CharField(blank=True, max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='order',
            name='model',
            field=models.CharField(blank=True, max_length=255, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
    ]
