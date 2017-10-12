from django.contrib import admin
from main.models import StudentRegisterationForm
from django.http import HttpResponse
import csv


def show_email(obj):
    email = obj.email
    return '<a href="mailto:%s" target="_blank">%s</a>' % (email, email)
show_email.allow_tags = True
show_email.short_description = 'Email'


def show_github_url(obj):
    github_url = obj.github_url
    return '<a href="%s" target="_blank">%s</a>' % (github_url, github_url)
show_github_url.allow_tags = True
show_github_url.short_description = 'GitHub URL'


class registerAdmin(admin.ModelAdmin):
    list_display = ('name', show_email, 'branch', 'year', show_github_url)
    actions = ['export_csv']

    class Meta:
        model = StudentRegisterationForm

    def export_csv(modeladmin, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="css_export.csv"'

        writer = csv.writer(response)
        for obj in queryset:
            writer.writerow([getattr(obj, f) for f in modeladmin.model._meta.fields])

        return response
    export_csv.short_description = "Export to CSV"

admin.site.register(StudentRegisterationForm, registerAdmin)
