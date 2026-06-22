from django.contrib import admin

from printpal_app.models import Printer, Filament, PrintJob, PrintUser

admin.site.register(PrintUser)
admin.site.register(Printer)
admin.site.register(Filament)
admin.site.register(PrintJob)
