import factory
from ...models import ExpenseGroup

class ExpenseGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ExpenseGroup
        
    name = factory.Sequence(lambda n: f'Expense Group {n}')

    @factory.post_generation
    def members(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for member in extracted:
                self.members.add(member)