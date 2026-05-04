from django.urls import path
from printpal_app.views import (
    Dashboard,
    FilamentsListView,
    FilamentsCreateView,
    FilamentsDeleteView,
    FilamentsEditView,
    MaterialCreateView,
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
        "material/create/",
        MaterialCreateView.as_view(),
        name="material-create"
    )
]

app_name = "printpal_app"
