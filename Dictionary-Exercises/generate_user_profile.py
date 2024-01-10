
from faker import Faker
import json

fake = Faker()

def generate_user_profile():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "birthdate": fake.date_of_birth().isoformat()
    }

user_profiles = [generate_user_profile() for _ in range(50)]

with open('user_profiles.json', 'w') as file:
    json.dump(user_profiles, file, indent=4)
