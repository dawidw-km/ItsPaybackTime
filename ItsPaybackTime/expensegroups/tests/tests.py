from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import ExpenseGroup
from users.tests.factories.user_factory import UserFactory
from expensegroups.tests.factories.expensegroup_factory import ExpenseGroupFactory

User = get_user_model()

class ExpenseGroupModelTest(TestCase):

    def test_create_expense_group(self):
        user = UserFactory.create()

        expense_group = ExpenseGroupFactory.create(
            created_by=user,
        )

        self.assertEqual(expense_group.name, 'Expense Group 0')
        self.assertEqual(expense_group.created_by, user)

    def test_deleted_user_is_none_expensegroup_exists_after_user_is_deleted(self):
        user = UserFactory.create()

        expense_group = ExpenseGroupFactory.create(
            created_by=user,
        )

        user.delete()
        expense_group.refresh_from_db()

        self.assertTrue(ExpenseGroup.objects.filter(id=expense_group.id).exists())
        self.assertIsNone(expense_group.created_by)
