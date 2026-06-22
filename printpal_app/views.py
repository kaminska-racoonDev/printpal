from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from printpal_app.models import (
    Filament,
    Printer,
    PrintJob,
    Brand
)

from printpal_app.forms import (
    FilamentForm,
    PrinterForm,
    BrandForm,
    PrintJobForm
)


# * DASHBOARD

class Dashboard(LoginRequiredMixin, generic.TemplateView):
    template_name = 'printpal_app/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context["printers"] = Printer.objects.filter(user=user)

        context["filaments_in_stock"] = Filament.objects.filter(
            user=user,
            amount__lt=2
        )

        context["filament_amount"] = Filament.objects.filter(
            user=user
        ).aggregate(total=Sum("amount"))["total"] or 0

        context["printjob_amount"] = PrintJob.objects.filter(
            user=user
        ).count()

        context["latest_printjobs"] = (
            PrintJob.objects.filter(user=user)
            .order_by("-id")[:3]
        )

        return context

# * FILAMENTS


class FilamentsListView(LoginRequiredMixin, generic.ListView):
    model = Filament
    template_name = 'printpal_app/filament_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Filament.objects.filter(user=self.request.user)


class FilamentsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Filament
    form_class = FilamentForm
    success_url = reverse_lazy('printpal_app:filament-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FilamentsEditView(LoginRequiredMixin, generic.UpdateView):
    model = Filament
    form_class = FilamentForm
    success_url = reverse_lazy('printpal_app:filament-list')

    def get_queryset(self):
        return Filament.objects.filter(user=self.request.user)


class FilamentsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Filament
    success_url = reverse_lazy('printpal_app:filament-list')

    def get_queryset(self):
        return Filament.objects.filter(user=self.request.user)


class FilamentAmountUpdateView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        filament = get_object_or_404(Filament, pk=pk, user=request.user)
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


# * PRINTERS

class PrinterListView(LoginRequiredMixin, generic.ListView):
    model = Printer
    template_name = 'printpal_app/printer_list.html'

    def get_queryset(self):
        return Printer.objects.filter(user=self.request.user)


class PrinterCreateView(LoginRequiredMixin, generic.CreateView):
    model = Printer
    form_class = PrinterForm
    success_url = reverse_lazy('printpal_app:printer-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PrinterUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Printer
    form_class = PrinterForm
    success_url = reverse_lazy('printpal_app:printer-list')

    def get_queryset(self):
        return Printer.objects.filter(user=self.request.user)


class PrinterDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Printer
    success_url = reverse_lazy('printpal_app:printer-list')

    def get_queryset(self):
        return Printer.objects.filter(user=self.request.user)


# * PRINT JOBS

class PrintJobListView(LoginRequiredMixin, generic.ListView):
    model = PrintJob
    template_name = 'printpal/printjob_list.html'

    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user)


class PrintJobDetailView(LoginRequiredMixin, generic.DetailView):
    model = PrintJob
    context_object_name = "job"

    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user)


class PrintJobCreateView(LoginRequiredMixin, generic.CreateView):
    model = PrintJob
    form_class = PrintJobForm
    success_url = reverse_lazy('printpal_app:printjob-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PrintJobUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PrintJob
    form_class = PrintJobForm
    success_url = reverse_lazy('printpal_app:printjob-list')

    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user)


class PrintJobDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PrintJob
    success_url = reverse_lazy('printpal_app:printjob-list')

    def get_queryset(self):
        return PrintJob.objects.filter(user=self.request.user)


# * BRAND

class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    template_name = "printpal_app/brand_list.html"

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)


class BrandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Brand
    template_name = "printpal_app/brand_detail.html"

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('printpal_app:brands-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('printpal_app:brands-list')

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy('printpal_app:brands-list')

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)
