# DjangoImports
from django.db import models
# End DjangoImports


# Config
class News(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
# End Config
