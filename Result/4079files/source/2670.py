import pytest
import random
from pyshare import group, party, expense, payment

# Create test data.

group_names = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", 'Juliett',
               "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango",
               "Uniform", "Victor", "Whisky", "XRay", "Yankee", "Zulu"]

party_names = ["Michael", "Callie", "Brian", "Robert", "Viki", "Daniel", "Colin", "Trudy", "Beth", 'Rajesh',
               "Savita", "Lindsay", "Matthew", "Kiel", "Kyle", "Chris", "Carol", "Jason", "Lisa", "Guy",
               "Kala", "Ricky", "Taylor", "Xavier", "Yvette", "Zane"]

expense_types = ["Rent", "Groceries", "Maintenance", "Hotel", "Cat Litter", "Cable", "Internet", "Credit Card"
                 "Power", "Dry Cleaning", "Diapers"]

currency_types = ["USD", "EUR", "BRL", "CAD", "GBP", "HRK", "JPY", "NOK", "NZD", "PHP", "RON", "RUB", "TRY", "ZAR"]


# Create helper functions for generating random test data.


def rand_group() -> group.Group:
    return group.Group(name=random.choice(group_names), currency=random.choice(currency_types))


def rand_party() -> party.Party:
    return party.Party(name=random.choice(party_names))


def rand_expense() -> expense.Expense:
    return expense.Expense(paid_for=random.choice(expense_types), currency=random.choice(currency_types),
                           amount=random.uniform(1.00, 999.99))


def rand_payment(e: expense.Expense) -> payment.Payment:
    return payment.Payment(expense=e, paid_by=random.choice(e.parties_involved), currency=e.currency,
                           amount=e.amount)


class TestGroup:

    @classmethod
    def setup_class(cls):
        cls.test_group = group.Group(name="Test", currency="USD")
        cls.not_a_party = "This is not a party.Party, it's a string."
        cls.test_party = party.Party(name="Michael")
        cls.not_an_expense = ["This is not an expense.Expense, it's a list."]
        cls.test_expense = expense.Expense(paid_for="Impulse purchase", currency="USD", amount=153.19)
        cls.not_a_payment = {"This is not a payment.Payment": "This is a dict."}
        cls.test_payment = payment.Payment(expense=cls.test_expense, paid_by=cls.test_party, currency="USD", amount=10)

    def test_assertion_error_if_add_not_party(self):
        with pytest.raises(AssertionError):
            self.test_group.add_party(self.not_a_party)

    def test_no_error_if_add_party(self):
        self.test_group.add_party(self.test_party)
        assert len(self.test_group.parties) == 1

    def test_assertion_error_if_add_not_expense(self):
        with pytest.raises(AssertionError):
            self.test_group.add_expense(self.not_an_expense)

    def test_no_error_if_add_expense(self):
        self.test_group.add_expense(self.test_expense)
        assert len(self.test_group.expenses) == 1

    def test_assertion_error_if_add_not_payment(self):
        with pytest.raises(AssertionError):
            self.test_group.add_payment(self.not_a_payment)

    def test_no_error_if_add_payment(self):
        self.test_group.add_payment(self.test_payment)
        assert len(self.test_group.payments) == 1

    def test_add_expense_to_group_also_adds_parties(self):
        # Set up new data for this test and make sure no parties in group
        new_group = rand_group()
        new_expense = rand_expense()
        new_party = rand_party()
        assert not new_group.parties

        # Add party to expense, then add expense to group
        new_expense.add_party(new_party)
        new_group.add_expense(new_expense)

        # Ensure expense party added to group
        assert len(new_group.parties) == 1

    def test_standardize_group_expenses(self):
        g = rand_group()
        expenses = {rand_expense(), rand_expense(), rand_expense(), rand_expense()}
        for e in expenses:
            g.add_expense(e)

        # Currencies should not match
        assert not g.currencies_match()

        g.standardize_group_expenses()

        # Now, expense currencies should match that of the group
        assert g.currencies_match()

    def test_standardize_group_expenses_and_payments(self):
        g = rand_group()
        # Add random expenses and linked payments
        for i in range(5):
            e = rand_expense()
            e.add_party(rand_party())
            g.add_expense(e)
            g.add_payment(rand_payment(e))

        # Currencies should not match
        assert not g.currencies_match()

        g.standardize_group_expenses()
        g.standardize_group_payments()

        # Now, expense and payment currencies should match that of the group
        assert g.currencies_match()

