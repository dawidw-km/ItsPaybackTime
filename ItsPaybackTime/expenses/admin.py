from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'expense_group', 'who_paid')
    list_filter = ('expense_group', 'who_paid')

admin.site.register(Expense, ExpenseAdmin)
