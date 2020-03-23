from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class SiteSettings(BaseSetting):
    phone = models.CharField(max_length=255, blank=True)
    # address = models.CharField(
    #     max_length=255, blank=True)
    work_time = models.CharField(max_length=255, blank=True)
    slogan_top = models.CharField(max_length=255, blank=True)
    slogan_bottom = models.CharField(max_length=255, blank=True)
    text_bottom = models.CharField(max_length=255, blank=True)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        ImageChooserPanel("logo"),
        FieldPanel("phone"),
        FieldPanel("work_time"),
        FieldPanel("slogan_top"),
        FieldPanel("slogan_bottom"),
        FieldPanel("text_bottom"),
    ]
