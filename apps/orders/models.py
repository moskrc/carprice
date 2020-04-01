from django.db import models


class Order(models.Model):
    """
    Заказ с форм
    """
    brand = models.CharField('Марка', max_length=255, blank=True)
    model = models.CharField('Модель', max_length=255, blank=True)
    year = models.CharField('Год выпуска', max_length=4, blank=True)
    phone = models.CharField('Телефон', max_length=255)
    name = models.CharField('Имя', max_length=255, blank=True)
    message = models.CharField('Комментарий', max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.phone)
