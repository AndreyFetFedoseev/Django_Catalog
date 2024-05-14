import json

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """
        Получаем данные из фикстур с категориями
        """
    # Здесь мы получаем данные из фикстур с категориями
    with open('catalog/fixture/catalog_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    def handle(self, *args, **options):
        # Удалите все продукты
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте список для хранения объектов
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(название_поля=значение_из_словаря, ..., название_поля=значение_из_словаря)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
