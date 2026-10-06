from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import ExpenseGroup

User = get_user_model()

class ExpenseGroupModelTest(TestCase):

    def create_user(self, email, username):
        return User.objects.create_user(
            username=username,
            email=email,
            password='testpassword123'
        )
    
    def test_create_expense_group(self):
        user = self.create_user(
            email='user@example.com',
            username='testuser'
        )

        expense_group = ExpenseGroup.objects.create(
            name='Test Expense Group',
            created_by=user,
        )


        self.assertEqual(expense_group.name, 'Test Expense Group')
        self.assertEqual(expense_group.created_by, user)
        self.assertEqual(expense_group.members.count(), 0)

    def test_deleted_user_is_none_expensegroup_exists_after_user_is_deleted(self):
        user = self.create_user(
            username='testuser',
            email='testuser@example.com'
        )

        expense_group = ExpenseGroup.objects.create(
            name='Test Expense Group',
            created_by=user,
        )

        user.delete()
        expense_group.refresh_from_db()

        self.assertTrue(ExpenseGroup.objects.filter(id=expense_group.id).exists())
        self.assertIsNone(expense_group.created_by)
