from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.email())

data = {
    'email': fake.email(),
    'first_name': fake.first_name(),
    'last_name': fake.last_name(),
}

print(data)