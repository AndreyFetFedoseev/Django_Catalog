from django.forms import ModelForm, forms

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        word_danger = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in word_danger:
            raise forms.ValidationError('Название запрещено. Введите другое название!')
        return cleaned_data

    def clean_description(self):
        word_danger = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        cleaned_data = self.cleaned_data['description']
        cleaned_data_sort = cleaned_data.lower().replace(',', "").split()
        if list(set(cleaned_data_sort) & set(word_danger)):
            raise forms.ValidationError('Использованы запрещенные слова!')
        return cleaned_data
