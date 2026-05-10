from django import forms
from .models import (
    Filament,
    Printer,
    Brand,
    PrintJob
)


class FilamentForm(forms.ModelForm):
    class Meta:
        model = Filament
        fields = [
            'brand',
            'weight',
            'color',
            'material',
            'amount',
            'color_code',
            'priority'
            # 'status'
        ]
        widgets = {
            'color_code': forms.TextInput(attrs={'type': 'color'})
        }


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = [
            'name',
            'model_name',
            'status'
        ]


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"


class PrintJobForm(forms.ModelForm):
    class Meta:
        model = PrintJob
        fields = "__all__"
        widgets = {
            "filament": forms.CheckboxSelectMultiple(),
        }
