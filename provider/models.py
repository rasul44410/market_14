from django.db import models


class Provider(models.Model):
    name = models.CharField(verbose_name="Yitkazib beruvchi", max_length=255)
    phone = models.CharField(verbose_name="Telefon", max_length=13)
    balance = models.DecimalField(verbose_name="Yitkazib beruvchi balansi", max_digits=17, decimal_places=2)
    info = models.TextField(verbose_name="Yitkazib beruvchi haqida ma'lumot")

    def str(self):
        return self.name

class Income(models.Model):
    data = models.DateTimeField(verbose_name="Yaratilgan vaqt", auto_now=True)
    provider = models.ForeignKey('Provider', verbose_name="Yitkizib beruvchi",
                                 on_delete=models.PROTECT)
    total = models.DecimalField(verbose_name="Summa", max_digits=17, decimal_places=2)

    def str(self):
        return f"{self.data}"


class IncomeItem(models.Model):
    income = models.ForeignKey("Income", on_delete=models.PROTECT)
    product = models.ForeignKey("product.Product", verbose_name="Maxsulot",
                                on_delete=models.PROTECT)
    count = models.SmallIntegerField(verbose_name="Soni")
    self_price = models.DecimalField(verbose_name="Maxsulot kelish narxi",
                                     max_digits=17, decimal_places=2, null=True)

    def str(self):
        return self.product.name