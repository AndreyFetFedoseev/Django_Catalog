from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """
    Модель для категории товаров
    """

    name = models.CharField(max_length=50, verbose_name="Категория", help_text="Введите категорию товара")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание категории", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """
    Модель для товаров
    """

    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.TextField(verbose_name="Описание", help_text="Введите описание товара", **NULLABLE)
    image = models.ImageField(
        upload_to="catalog/products",
        verbose_name="Изображение товара",
        help_text="Загрузите изображение товара",
        **NULLABLE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите название категории",
        related_name="products",
    )
    price = models.PositiveIntegerField(verbose_name="Цена за покупку", help_text="Введите цену")
    created_at = models.DateField(verbose_name="Дата создания", help_text="Введите дату", auto_now_add=True)
    update_at = models.DateField(verbose_name="Дата изменения", help_text="Введите дату", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category", "price"]
