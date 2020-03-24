from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Order


class OrderModelAdmin(ModelAdmin):
    model = Order
    menu_label = "Заказы"
    menu_icon = "date"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = (
        False
    )
    list_display = ("car", "phone", "year", "created")
    list_filter = ("car", )
    search_fields = ("car", "phone", "year", )


modeladmin_register(OrderModelAdmin)
