from django.contrib import admin
from main.models import StudentRegisterationForm

class registerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'branch', 'year', 'github_url')
    class Meta:
        model = StudentRegisterationForm

admin.site.register(StudentRegisterationForm, registerAdmin)