# Generated by Django 3.0.5 on 2020-04-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200402_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='new_order_emails',
            field=models.CharField(blank=True, help_text='Список email адресов через запятую', max_length=255),
        ),
    ]