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
        help_text="Выберите категорию",
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


class Blog(models.Model):
    """
    Модель для блога
    """

    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name="Содержимое", **NULLABLE)
    preview = models.ImageField(
        upload_to="blog/", verbose_name="Отправить изображение", **NULLABLE
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    publication = models.BooleanField(verbose_name="Опубликовано", default=True)
    number_of_views = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]


class Version(models.Model):
    """
    Модель для версий товаров
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, verbose_name='Товар', **NULLABLE)
    number_version = models.PositiveIntegerField(verbose_name='Номер версии', default=1)
    name_version = models.CharField(max_length=255, verbose_name='Название версии')
    current_version_indicator = models.BooleanField(verbose_name='Признак текущей версии', default=True)

    def __str__(self):
        return self.name_version

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
