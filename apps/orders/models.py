from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from wagtail.contrib.settings.context_processors import SettingsProxy
from wagtail.core.models import Site
from apps.core.helpers import send_email


class Order(models.Model):
    """
    Заказ с форм
    """

    brand = models.CharField("Марка", max_length=255, blank=True)
    model = models.CharField("Модель", max_length=255, blank=True)
    year = models.CharField("Год выпуска", max_length=4, blank=True)
    phone = models.CharField("Телефон", max_length=255)
    name = models.CharField("Имя", max_length=255, blank=True)
    message = models.CharField("Комментарий", max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.phone)


@receiver(post_save, sender=Order)
def send_new_order(sender, **kwargs):
    instance = kwargs.get("instance")

    wagtail_settings = SettingsProxy(Site.objects.get(is_default_site=True))
    project_settings = wagtail_settings["core"]["SiteSettings"]
    emails = [x.strip() for x in project_settings.new_order_emails.split(",")]

    send_email(
        subject="Новое сообщение",
        template_file="orders/email/new_order.html",
        context={"order": instance},
        to_email=emails,
        from_email=project_settings.email
    )
