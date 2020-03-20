from django.db import models

from wagtail.core.models import Page
from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import RichTextField, StreamBlock, StreamField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from apps.core.blocks import FeaturesBlock, ActionBlock, CarsBlock, StepsBlock


CONTENT_STREAMBLOCKS = [
    ("features", FeaturesBlock()),
    ("action", ActionBlock()),
    ("cars", CarsBlock()),
	("steps", StepsBlock()),
]


class HomePage(Page):
    body = StreamField(CONTENT_STREAMBLOCKS, null=True, blank=True)
    content_panels = Page.content_panels + [
        StreamFieldPanel("body")
    ]
