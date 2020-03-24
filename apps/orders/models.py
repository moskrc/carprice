from django.db import models


class Order(models.Model):
    """
    Заказ с форм
    """
    car = models.CharField('Автмобиль', max_length=255)
    year = models.CharField('Год выпуска', max_length=4, blank=True)
    phone = models.CharField('Телефон', max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.phone)
