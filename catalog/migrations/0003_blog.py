# Generated by Django 5.0.6 on 2024-05-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите заголовок', max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                (
                    'content',
                    models.TextField(blank=True, help_text='Напишите статью', null=True, verbose_name='Содержимое'),
                ),
                (
                    'preview',
                    models.ImageField(
                        blank=True,
                        help_text='Выберите изображение',
                        null=True,
                        upload_to='blog/',
                        verbose_name='Отправить изображение',
                    ),
                ),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('publication', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('number_of_views', models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ['created_at'],
            },
        ),
    ]
