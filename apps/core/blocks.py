from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ButtonBlock(blocks.StructBlock):
    """Кнопка"""

    text = blocks.CharBlock()
    page_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "link"
        template = "blocks/button_block.html"


class FeaturesBlock(blocks.StructBlock):
    """Панель с возможностями"""

    title = blocks.CharBlock()
    features = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("image", ImageChooserBlock(required=True)),
                ("text", blocks.CharBlock(required=True, max_length=255)),
            ]
        )
    )

    class Meta:
        icon = "link"
        template = "blocks/features_block.html"


class ActionBlock(blocks.StructBlock):
    """Панель с кнопкой к действию"""

    title = blocks.CharBlock()
    text = blocks.CharBlock(required=True, max_length=255)
    button = ButtonBlock()

    class Meta:
        icon = "link"
        template = "blocks/action_block.html"


class CarsBlock(blocks.StructBlock):
    """Панель с купленными машинами"""

    title = blocks.CharBlock()
    cars = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("price", blocks.CharBlock(required=True, max_length=255)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("image", ImageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        icon = "link"
        template = "blocks/cars_block.html"


class StepsBlock(blocks.StructBlock):
    """Панель с шагами"""

    title = blocks.CharBlock()
    steps = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("number", blocks.CharBlock(required=True, max_length=2)),
                ("title", blocks.CharBlock(required=True, max_length=100)),
                ("text", blocks.CharBlock(required=True, max_length=255)),
            ]
        )
    )

    class Meta:
        icon = "link"
        template = "blocks/steps_block.html"


class MapBlock(blocks.StructBlock):
    """Панель с картой"""

    yandex_map = blocks.TextBlock(help_text="Код из конструктора Яндекс карт")
    text = blocks.RichTextBlock()
    show_phone = blocks.BooleanBlock(required=False)
    show_work_time = blocks.BooleanBlock(required=False)

    class Meta:
        icon = "map"
        template = "blocks/map_block.html"
