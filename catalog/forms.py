from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner')

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


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'publication')


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    # def clean_current_version_indicator(self):
    #     # data = 0
    #     cleaned_data = self.cleaned_data
    #
    #     # if cleaned_data:
    #     #     cleaned_data += cleaned_data
    #     print(cleaned_data)
    #     # if cleaned_data['current_version_indicator']:
    #     #     if cleaned_data['current_version_indicator']:
    #             # raise forms.ValidationError('Название запрещено. Введите другое название!')
    #     # return cleaned_data