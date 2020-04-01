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
    list_display = ("phone", "brand", "model", "year",  "name", "message", "created")
    search_fields = ("name", "phone", "message", "brand", "model", "year" )

modeladmin_register(OrderModelAdmin)
