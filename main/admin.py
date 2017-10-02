from django.contrib import admin
from main.models import StudentRegisterationForm
from django.http import HttpResponse
import csv

class registerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'branch', 'year', 'github_url')
    actions = ['export_csv']
    class Meta:
        model = StudentRegisterationForm

    def export_csv(modeladmin, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="css_export.csv"'

        writer = csv.writer(response)
        for obj in queryset:
            writer.writerow([getattr(obj, f) for f in modeladmin.list_display])

        return response
    export_csv.short_description = "Export to CSV"

admin.site.register(StudentRegisterationForm, registerAdmin)