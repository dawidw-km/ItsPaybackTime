from django.contrib import admin
from .models import ExpenseGroup

class ExpenseGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')

admin.site.register(ExpenseGroup, ExpenseGroupAdmin)
