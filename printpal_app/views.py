from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from printpal_app.models import (
    Filament,
    # Material,
    Printer,
    PrintUser,
    PrintJob,
    MyPrintPal,
    Brand
)
from printpal_app.forms import (
    FilamentForm,
    PrinterForm,
    BrandForm,
    PrintJobForm
)


class Dashboard(generic.TemplateView):
    template_name = 'printpal_app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["printers"] = Printer.objects.all()

        context["filaments_in_stock"] = Filament.objects.all()

        context["latest_printjobs"] = (
            PrintJob.objects.order_by("-id")[:3]
        )

        return context


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


class FilamentAmountUpdateView(generic.View):
    def post(self, request, pk):
        filament = get_object_or_404(Filament, pk=pk)
        action = request.POST.get("action")

        if action == "increase":
            filament.amount += 1
        elif action == "decrease":
            if filament.amount > 0:
                filament.amount -= 1
        elif action == "set":
            try:
                filament.amount = int(request.POST.get("amount"))
            except (TypeError, ValueError):
                pass

        filament.save()
        return redirect('printpal_app:filament-list')


# Printer


class PrinterListView(generic.ListView):
    model = Printer
    template_name = 'printpal_app/printer_list.html'


class PrinterCreateView(generic.CreateView):
    model = Printer
    form_class = PrinterForm
    success_url = reverse_lazy('printpal_app:printer-list')


class PrinterUpdateView(generic.UpdateView):
    model = Printer
    form_class = PrinterForm
    success_url = reverse_lazy('printpal_app:printer-list')


class PrinterDeleteView(generic.DeleteView):
    model = Printer
    success_url = reverse_lazy('printpal_app:printer-list')

# Material


# class MaterialListView(generic.ListView):
#     model = Material
#     template_name = 'printpal/material_list.html'


# class MaterialCreateView(generic.CreateView):
#     model = Material
#     form_class = MaterialForm
#     success_url = reverse_lazy('printpal_app:filament-list')


# class MaterialEditView(generic.UpdateView):
#     model = Material
#     form_class = MaterialForm
#     success_url = reverse_lazy('printpal_app:filament-list')

# Print job


class PrintJobListView(generic.ListView):
    model = PrintJob
    template_name = 'printpal/printjob_list.html'


class PrintJobDetailView(generic.DetailView):
    model = PrintJob
    context_object_name = "job"
    # template_name = 'printpal/printjob_detail.html'


class PrintJobCreateView(generic.CreateView):
    model = PrintJob
    form_class = PrintJobForm
    success_url = reverse_lazy('printpal_app:printjob-list')


class PrintJobUpdateView(generic.UpdateView):
    model = PrintJob
    form_class = PrintJobForm
    success_url = reverse_lazy('printpal_app:printjob-list')


class PrintJobDeleteView(generic.DeleteView):
    model = PrintJob
    success_url = reverse_lazy('printpal_app:printjob-list')

# Brand


class BrandListView(generic.ListView):
    model = Brand
    template_name = "printpal_app/brand_list.html"


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = "printpal_app/brand_detail.html"


class BrandCreateView(generic.CreateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('printpal_app:brands-list')


class BrandUpdateView(generic.UpdateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('printpal_app:brands-list')


class BrandDeleteView(generic.DeleteView):
    model = Brand
    success_url = reverse_lazy('printpal_app:brands-list')
