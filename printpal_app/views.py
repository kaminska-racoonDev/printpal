from django.views import generic
from django.urls import reverse_lazy
from .models import (
    Filament,
    Material,
    Printer,
    PrintUser,
    PrintJob,
    MyPrintPal,
)
from .forms import (
    FilamentForm,
    PrinterForm,
    MaterialForm,
)


class Dashboard(generic.TemplateView):
    template_name = 'printpal_app/dashboard.html'


class FilamentsListView(generic.ListView):
    model = Filament
    paginate_by = 6
    # ordering = ['-created_at']
    template_name = 'printpal_app/filament_list.html'


class FilamentsCreateView(generic.CreateView):
    model = Filament
    form_class = FilamentForm
    success_url = reverse_lazy('printpal_app:filament-list')


class FilamentsDeleteView(generic.DeleteView):
    model = Filament
    success_url = reverse_lazy('printpal:dashboard.html')


class FilamentsEditView(generic.UpdateView):
    model = Filament
    form_class = FilamentForm
    success_url = reverse_lazy('printpal_app:filament-list')

# Printer


class PrinterListView(generic.ListView):
    model = Printer
    template_name = 'printpal/printer_list.html'


class PrinterCreateView(generic.CreateView):
    model = Printer
    form_class = PrinterForm
    success_url = reverse_lazy('printpal:printer-list.html')


class PrinterDeleteView(generic.DeleteView):
    model = Filament
    success_url = reverse_lazy('printpal:printer-list.html')


class MaterialCreateView(generic.CreateView):
    model = Material
    form_class = MaterialForm
    success_url = reverse_lazy('printpal_app:filament-list')


class MaterialEditView(generic.UpdateView):
    model = Material
    form_class = MaterialForm
    success_url = reverse_lazy('printpal_app:filament-list')
