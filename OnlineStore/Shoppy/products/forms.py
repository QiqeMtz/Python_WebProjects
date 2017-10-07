from django import forms
from .models import Product
# derivado de ModelForm porque vamos a crear un formulario en base a un modelo ya existente dentro de nuestra aplicación
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'