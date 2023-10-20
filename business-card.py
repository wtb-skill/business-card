from faker import Faker
from typing import Type, List


class BaseContact:
    def __init__(self, name: str, surname: str, phone: str, email: str):
        """Initialize a basic contact."""
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        """Return a formatted string representation of the contact."""
        return f'{self.name} {self.surname}, {self.email}'

    def contact(self) -> None:
        """Simulate making contact using the private phone number."""
        print(f"Wybieram nr prywatny {self.phone} i dzwonię do {self.name} {self.surname}.")

    @property
    def label_length(self) -> int:
        """Calculate and return the length of the contact's name plus surname."""
        return len(self.name) + len(self.surname) + 1


class BusinessContact(BaseContact):
    def __init__(self, company: str, position: str, business_phone: str, *args, **kwargs):
        """
        Initialize a business contact.

        Inherits from BaseContact and adds company, position, and business phone.
        """
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.business_phone = business_phone

    def contact(self) -> None:
        """Simulate making contact using the business phone number."""
        print(f"Wybieram nr służbowy {self.business_phone} i dzwonię do {self.name} {self.surname}.")


def create_contacts(contact_type: Type[BaseContact], amount: int) -> List[BaseContact]:
    """
    Create a list of contacts based on the specified contact type and amount.

    :param contact_type: Type of contact (BaseContact or BusinessContact).
    :param amount: Number of contacts to create.
    :return: List of created contact instances.
    """
    fake = Faker(locale='pl')
    _contacts = []

    for _ in range(0, amount):
        fake_name = fake.first_name()
        fake_surname = fake.last_name()
        fake_phone = fake.phone_number()
        fake_email = fake.email()

        kwargs = {
            'name': fake_name,
            'surname': fake_surname,
            'email': fake_email,
            'phone': fake_phone
        }

        if issubclass(contact_type, BusinessContact):
            kwargs['company'] = fake.company()
            kwargs['position'] = fake.job()
            kwargs['business_phone'] = fake.phone_number()

        _contact = contact_type(**kwargs)
        _contacts.append(_contact)

    return _contacts


contacts = create_contacts(BaseContact, 2)
for contact in contacts:
    contact.contact()
contacts = create_contacts(BusinessContact, 2)
for contact in contacts:
    contact.contact()

