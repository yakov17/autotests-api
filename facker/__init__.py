import faker

def fake_info():
    fake = faker.Faker()

    payload = {
        "email": fake.unique.email(),
        "password": fake.password(length=12),
        "lastName": fake.last_name(),
        "firstName": fake.first_name(),
        "middleName": 'string',
    }

    return payload
