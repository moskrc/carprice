from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Orderable
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel

@register_snippet
class Car(models.Model):
    name = models.CharField(max_length=255, help_text='Например: Land-Cruiser 200 2010')
    image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    price = models.CharField(max_length=255, help_text='Например: 1 320 500 руб')

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('image'),
        FieldPanel('price'),
    ]

    def __str__(self):
        return self.name

    class Meta:  # noqa
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class CarPageOrderable(Orderable):    
    page = ParentalKey("home.HomePage", related_name="cars")
    car = models.ForeignKey(
        "snippets.Car",
        on_delete=models.CASCADE,
    )
    
    panels = [
        SnippetChooserPanel("car"),
    ]
            