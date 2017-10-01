from django.contrib import admin
from django.utils.html import format_html
from main.models import StudentRegisterationForm
from django.http import HttpResponse
import csv


class registerAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_email', 'branch', 'year', 'show_github_url')
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

    def show_github_url(obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.github_url)
    show_github_url.short_description = "GitHub URL"

    def show_email(obj):
        return format_html("<a href='mailto:{email}' target='_blank'>{email}</a>", email=obj.email)
    show_email.short_description = "Email"


admin.site.register(StudentRegisterationForm, registerAdmin)
