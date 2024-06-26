from faker import Faker

namea1=Faker('hi_IN')
for i in range(10):
    print(namea1.name() , namea1.date_of_birth(),namea1.phone_number(), namea1.email())

