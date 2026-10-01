from django.db import models
from django.conf import settings

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    expense_group = models.ForeignKey('expensegroups.ExpenseGroup', on_delete=models.CASCADE, related_name='expenses')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participated_expenses')
    who_paid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='paid_expenses')
