from faker import Faker
import json
import random

fake = Faker()

products = [{"name": fake.word(), "price": round(random.uniform(10, 1000), 2), "category": fake.word()} for _ in range(30)]

customers = []
for _ in range(20):
    customer = {
        "name": fake.name(),
        "email": fake.email(),
        "purchases": random.choices(products, k=random.randint(1, 10))
    }
    customers.append(customer)

ecommerce_data = {"products": products, "customers": customers}

with open('ecommerce_data.json', 'w') as file:
    json.dump(ecommerce_data, file, indent=4)

