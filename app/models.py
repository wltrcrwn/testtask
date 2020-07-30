from django.db import models


class Order(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField('Назва товару', max_length=255)

    def __str__(self):
        try:
            return self.product_name
        except:
            return str(self.id)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class Customer(models.Model):
    first_name = models.CharField('Імя', max_length=255)
    last_name = models.CharField('Прізвище', max_length=255)
    date_of_birth = models.DateField('Дата народження')
    register_date = models.DateField('Дата реєстрації')
    order = models.OneToOneField(Order, verbose_name='Замовлення', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        try:
            return f'{self.first_name} {self.last_name}, {self.register_date}'
        except:
            return str(self.id)

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
