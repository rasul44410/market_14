from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name="Ota kategoriyasi",
                               on_delete=models.PROTECT, blank=True, null=True)
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name='Mahsulot Categoriyasi',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Mahsulot nomi", max_length=255)
    full_name = models.CharField(verbose_name="Mahsulot toliq nomi", max_length=255,)
    price = models.DecimalField(verbose_name="Mahsulot narxi", max_digits=17, decimal_places=2)
    descriptions = models.TextField(verbose_name="Maxsulot haqida malumot")

    def __str__(self):
        return self.full_name