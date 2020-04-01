from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SiteSettings(BaseSetting):
    phone = models.CharField('Телефон', max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    work_time = models.CharField('Время работы', max_length=255, blank=True)
    slogan_top = models.CharField('Слоган - верх', max_length=255, blank=True)
    slogan_bottom = models.CharField('Слоган - низ', max_length=255, blank=True)
    text_bottom = models.CharField('Текст - низ', max_length=255, blank=True)
    logo_top = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name='Логотип - верх'
    )
    logo_bottom = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name='Логотип - низ'
    )

    panels = [
        ImageChooserPanel("logo_top"),
        ImageChooserPanel("logo_bottom"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("work_time"),
        FieldPanel("slogan_top"),
        FieldPanel("slogan_bottom"),
        FieldPanel("text_bottom"),
    ]
