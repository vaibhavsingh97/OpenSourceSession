from django.contrib import admin
from main.models import StudentRegisterationForm


def show_email(obj):
    email = obj.email
    return '<a href="mailto:%s" target="_blank">%s</a>' % (email, email)
show_email.short_description = 'Email'


def show_github_url(obj):
    github_url = obj.github_url
    return '<a href="%s" target="_blank">%s</a>' % (github_url, github_url)
show_github_url.short_description = 'GitHub URL'


class registerAdmin(admin.ModelAdmin):
    list_display = ('name', show_email, 'branch', 'year', show_github_url)

    class Meta:
        model = StudentRegisterationForm

admin.site.register(StudentRegisterationForm, registerAdmin)
