from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class MainBlock(blocks.StructBlock):
    """
    Главная панель
    """

    header1 = blocks.CharBlock(label="Первая линия заголовка")
    header2 = blocks.CharBlock(label="Вторая линия заголовка")
    header3 = blocks.CharBlock(label="Третья линия заголовка")
    items = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("text", blocks.CharBlock(required=True, max_length=255)),
            ]
        ),
        label="Список",
    )

    class Meta:
        icon = "main"
        template = "blocks/main_block.html"


class FeaturesBlock(blocks.StructBlock):
    """
    Панель с возможностями
    """

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
    """
    Панель с кнопкой к действию
    """

    title = blocks.CharBlock(label="Заголовок")
    text = blocks.RichTextBlock(label="Содержимое")
    button_text = blocks.CharBlock(label="Текст кнопки")

    class Meta:
        icon = "link"
        template = "blocks/action_block.html"


class CarsBlock(blocks.StructBlock):
    """
    Панель с купленными машинами
    """

    title = blocks.CharBlock()
    cars = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    "title",
                    blocks.CharBlock(
                        label="Название автомобиля",
                        required=True,
                        max_length=100,
                        help_text="Например: Nissian Teana",
                    ),
                ),
                (
                    "year",
                    blocks.CharBlock(
                        label="Год выпуска",
                        required=True,
                        max_length=100,
                        help_text="Например: 2008",
                    ),
                ),
                (
                    "engine",
                    blocks.CharBlock(
                        label="Объем двигателя",
                        required=True,
                        help_text="Объем в литрах, например: 1.5",
                    ),
                ),
                (
                    "gear",
                    blocks.ChoiceBlock(
                        label="Трансмиссия",
                        required=True,
                        choices=(
                            ("МКПП", "МКПП"),
                            ("АКПП", "АКПП"),
                            ("Вариатор", "Вариатор"),
                        ),
                        help_text="Вид трансмиссии",
                    ),
                ),
                (
                    "price",
                    blocks.CharBlock(
                        label="Цена",
                        required=True,
                        max_length=255,
                        help_text="Цена в рублях с пробелами",
                    ),
                ),
                (
                    "image",
                    ImageChooserBlock(
                        label="Фотография",
                        required=True,
                        help_text="Изображение автомобиля",
                    ),
                ),
                (
                    "logo",
                    ImageChooserBlock(
                        label="Логотип",
                        required=True,
                        help_text="Логотип производителя",
                    ),
                ),
            ]
        )
    )

    class Meta:
        icon = "link"
        template = "blocks/cars_block.html"


class StepsBlock(blocks.StructBlock):
    """
    Панель с шагами
    """

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


class FormBlock(blocks.StructBlock):
    """
    Панель с формой на фоне машины внизу
    """

    title = blocks.CharBlock()

    class Meta:
        icon = "form"
        template = "blocks/form_block.html"


class MapBlock(blocks.StructBlock):
    """
    Панель с картой
    """

    yandex_map = blocks.TextBlock(help_text="Код из конструктора Яндекс карт")
    text = blocks.RichTextBlock(required=False)
    show_phone = blocks.BooleanBlock(required=False)
    show_work_time = blocks.BooleanBlock(required=False)

    class Meta:
        icon = "map"
        template = "blocks/map_block.html"
