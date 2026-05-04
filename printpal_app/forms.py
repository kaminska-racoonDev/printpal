from django import forms
from .models import Filament, Printer, Material


class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = [
            'brand',
            'weight',
            'color',
            'material',
            'amount'
            # 'status'
        ]
    # widgets {
    #     'status'
    # }


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = [
            'name',
            'model_name',
            'status'
        ]


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'name'
        ]
