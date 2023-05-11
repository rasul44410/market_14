# Generated by Django 4.2.1 on 2023-05-11 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan vaqt')),
                ('total', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Summa')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Yitkazib beruvchi')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=17, verbose_name='Yitkazib beruvchi balansi')),
                ('info', models.TextField(verbose_name="Yitkazib beruvchi haqida ma'lumot")),
            ],
        ),
        migrations.CreateModel(
            name='IncomeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField(verbose_name='Soni')),
                ('self_price', models.DecimalField(decimal_places=2, max_digits=17, null=True, verbose_name='Maxsulot kelish narxi')),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.income')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product', verbose_name='Maxsulot')),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='provider.provider', verbose_name='Yitkizib beruvchi'),
        ),
    ]