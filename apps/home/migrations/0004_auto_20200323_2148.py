# Generated by Django 3.0.4 on 2020-03-23 18:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('features', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('features', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))])), ('action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('page_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cars', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('cars', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('price', wagtail.core.blocks.CharBlock(max_length=255, required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('steps', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('steps', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.CharBlock(max_length=2, required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=True))])))])), ('map', wagtail.core.blocks.StructBlock([('yandex_map', wagtail.core.blocks.TextBlock(help_text='Код из конструктора Яндекс карт')), ('text', wagtail.core.blocks.RichTextBlock()), ('show_phone', wagtail.core.blocks.BooleanBlock(required=False)), ('show_work_time', wagtail.core.blocks.BooleanBlock(required=False))]))], blank=True, null=True),
        ),
    ]
