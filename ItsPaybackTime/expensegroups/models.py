from django.db import models
from django.conf import settings

class ExpenseGroup(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_expense_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='expense_groups')

    def __str__(self):
        return f"ExpenseGroup(name={self.name}, created_by={self.created_by if self.created_by else 'User do not exist'}, created_at={self.created_at}, members={[member.username for member in self.members.all()]})"

            
