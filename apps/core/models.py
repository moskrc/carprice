from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SiteSettings(BaseSetting):
    phone = models.CharField("Телефон", max_length=255, blank=True)
    address = models.CharField("Адрес", max_length=255, blank=True)
    email = models.EmailField("Email", blank=True)
    new_order_emails = models.CharField(
        "Адреса",
        max_length=255,
        blank=True,
        help_text="Список email адресов через запятую",
    )
    work_time = models.CharField("Время работы", max_length=255, blank=True)
    slogan_top = models.CharField("Слоган - верх", max_length=255, blank=True)
    slogan_bottom = models.CharField("Слоган - низ", max_length=255, blank=True)
    text_bottom = models.CharField("Текст - низ", max_length=255, blank=True)
    logo_top = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Логотип - верх",
    )
    logo_bottom = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Логотип - низ",
    )

    panels = [
        MultiFieldPanel(
            [
                ImageChooserPanel("logo_top"),
                ImageChooserPanel("logo_bottom"),
                FieldPanel("slogan_top"),
                FieldPanel("slogan_bottom"),
                FieldPanel("text_bottom"),
            ],
            heading="Логотипы, шапка, подвал",
        ),
        MultiFieldPanel(
            [
                FieldPanel("phone"),
                FieldPanel("email"),
                FieldPanel("address"),
                FieldPanel("work_time"),
            ],
            heading="Реквизиты",
        ),
        MultiFieldPanel(
            [FieldPanel("new_order_emails"),], heading="Уведомление о новых сообщениях",
        ),
    ]
