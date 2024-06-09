# Generated by Django 5.0.6 on 2024-06-09 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_blog_content_alter_blog_preview_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.PositiveIntegerField(default=1, verbose_name='Номер версии')),
                ('name_version', models.CharField(max_length=255, verbose_name='Название версии')),
                ('current_version_indicator', models.BooleanField(default=True, verbose_name='Признак текущей версии')),
                (
                    'product',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='catalog.product',
                        verbose_name='Товар',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
