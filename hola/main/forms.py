from .models import Word
from django.forms import ModelForm, TextInput


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ["word", "translate"]
        widgets = {
            "word": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите слово'
            }),
            "translate": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите перевод'})
        }

