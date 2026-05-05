from django.urls import path
from printpal_app.views import (
    Dashboard,
    FilamentsListView,
    FilamentsCreateView,
    FilamentsDeleteView,
    FilamentsEditView,
    # MaterialCreateView,
    FilamentAmountUpdateView,
    PrintJobListView,
    PrintJobCreateView,
    PrintJobDeleteView,
    PrintJobUpdateView,
    PrintJobDetailView,
    # MaterialListView,
    PrinterListView,
    PrinterCreateView,
    PrinterUpdateView,
    PrinterDeleteView,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    BrandDetailView
)


urlpatterns = [
    path(
        "",
        Dashboard.as_view(),
        name="dashboard"
    ),
    path(
        "filaments/",
        FilamentsListView.as_view(),
        name="filament-list"
    ),
    path(
        "filament/create/",
        FilamentsCreateView.as_view(),
        name="filament-create"),
    path(
        "filament/<int:pk>/delete/",
        FilamentsDeleteView.as_view(),
        name="filament-delete"),
    path(
        "filament/<int:pk>/edit/",
        FilamentsEditView.as_view(),
        name="filament-edit"),
    path(
        "filament/<int:pk>/amount/",
        FilamentAmountUpdateView.as_view(),
        name="filament-amount"
    ),
    # path(
    #     "material/create/",
    #     MaterialCreateView.as_view(),
    #     name="material-create"
    # ),
    path(
        "printjobs/",
        PrintJobListView.as_view(),
        name="printjob-list"
    ),
    path(
        "printjob/create/",
        PrintJobCreateView.as_view(),
        name="printjob-create"
    ),
    path(
        "printjob/<int:pk>/edit/",
        PrintJobUpdateView.as_view(),
        name="printjob-edit"
    ),
    path(
        "printjob/<int:pk>/delete/",
        PrintJobDeleteView.as_view(),
        name="printjob-delete"
    ),
    path(
        "printjob/<int:pk>/",
        PrintJobDetailView.as_view(),
        name="printjob-detail"
    ),
    # path(
    #     "materials/",
    #     MaterialListView.as_view(),
    #     name="material-list"
    # ),
    path(
        "printers/",
        PrinterListView.as_view(),
        name="printer-list"
    ),
    path(
        "printer/create/",
        PrinterCreateView.as_view(),
        name="printer-create"
    ),
    path(
        "printer/<int:pk>/edit/",
        PrinterUpdateView.as_view(),
        name="printer-edit"
    ),
    path(
        "printer/<int:pk>/delete/",
        PrinterDeleteView.as_view(),
        name="printer-delete"
    ),
    path(
        "brands/",
        BrandListView.as_view(),
        name="brands-list"
    ),
    path(
        "brand/create",
        BrandCreateView.as_view(),
        name="brand-create"
    ),
    path(
        "brand/<int:pk>/detail/",
        BrandDetailView.as_view(),
        name="brand-detail"
    ),
    path(
        "brand/<int:pk>/edit",
        BrandUpdateView.as_view(),
        name="brand-edit"
    ),
    path(
        "brand/<int:pk>/delete",
        BrandDeleteView.as_view(),
        name="brand-delete"
    ),
]

app_name = "printpal_app"
