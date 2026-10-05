from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Expense
from expensegroups.models import ExpenseGroup

User = get_user_model()

class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = self.create_user(
            email='test@example.com',
            username='testuser'
        )

        self.expense_group = self.create_expense_group(
            name='Test Expense Group',
            created_by=self.user
        )

        self.expense = self.create_expense(
            description='Test Expense',
            amount=Decimal('100.00'),
            expense_group=self.expense_group,
            who_paid=self.user
        )

    ### Helper methods to create test data

    def create_user(self, email, username):
        return User.objects.create_user(
            username=username,
            email=email,
            password='testpassword123'
        )

    def create_expense_group(self, name, created_by):
        return ExpenseGroup.objects.create(
            name=name,
            created_by=created_by
        )

    def create_expense(self, description, amount, expense_group, who_paid):
        return Expense.objects.create(
            description=description,
            amount=amount,
            expense_group=expense_group,
            who_paid=who_paid
        )

    ### Test cases

    def test_expense_group_cascade_delete_expense_after_group_is_deleted(self):
        self.expense_group.delete()

        with self.assertRaises(Expense.DoesNotExist):
            Expense.objects.get(id=self.expense.id)
    
    def test_deleted_user_is_null_expense_exists_after_user_is_deleted(self):
        self.user.delete()
        self.expense.refresh_from_db()
        self.assertIsNone(self.expense.who_paid)