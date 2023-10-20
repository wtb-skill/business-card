from faker import Faker


class BusinessCard:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email

    def __str__(self):
        return f'{self.name} {self.surname}, {self.position}, {self.email}'

    def contact(self):
        print(f"Kontaktuję się z {self.__str__()}.")

    @property
    def length_of_name_and_surname(self):
        return len(self.name) + len(self.surname) + 1


fake = Faker(locale='pl')


business_cards = []
for i in range(0, 5):
    fake_name = fake.first_name()
    fake_surname = fake.last_name()
    fake_company = fake.company()
    fake_position = fake.job()
    fake_email = fake.email()
    business_card = BusinessCard(
        name=fake_name,
        surname=fake_surname,
        company=fake_company,
        position=fake_position,
        email=fake_email
    )
    business_cards.append(business_card)

# for card in business_cards:
#     print("Name:", card.name)
#     print("Surname:", card.surname)
#     print("Company:", card.company)
#     print("Position:", card.position)
#     print("Email:", card.email)
#     print()

business_cards[0].contact()
print(business_cards[0].length_of_name_and_surname)
