# Generated by Django 5.0.6 on 2024-05-16 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'name',
                    models.CharField(help_text='Введите категорию товара', max_length=50, verbose_name='Категория'),
                ),
                (
                    'description',
                    models.TextField(
                        blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'name',
                    models.CharField(
                        help_text='Введите наименование товара', max_length=50, verbose_name='Наименование'
                    ),
                ),
                (
                    'description',
                    models.TextField(
                        blank=True, help_text='Введите описание товара', null=True, verbose_name='Описание'
                    ),
                ),
                (
                    'image',
                    models.ImageField(
                        blank=True,
                        help_text='Загрузите изображение товара',
                        null=True,
                        upload_to='catalog/media',
                        verbose_name='Изображение товара',
                    ),
                ),
                ('price', models.PositiveIntegerField(help_text='Введите цену', verbose_name='Цена за покупку')),
                (
                    'created_at',
                    models.DateField(auto_now_add=True, help_text='Введите дату', verbose_name='Дата создания'),
                ),
                ('update_at', models.DateField(auto_now=True, help_text='Введите дату', verbose_name='Дата изменения')),
                (
                    'category',
                    models.ForeignKey(
                        help_text='Введите название категории',
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='products',
                        to='catalog.category',
                        verbose_name='Категория',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['category', 'price'],
            },
        ),
    ]
