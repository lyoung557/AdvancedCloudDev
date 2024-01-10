from faker import Faker
import json
from collections import Counter
from datetime import datetime

fake = Faker()

medical_records = []
for _ in range(100):
    record = {
        "patient_name": fake.name(),
        "doctor_name": fake.name(),
        "visit_date": fake.date_between(start_date='-2y', end_date='today').isoformat(),
        "diagnosis": fake.sentence()
    }
    medical_records.append(record)

with open('medical_records.json', 'w') as file:
    json.dump(medical_records, file, indent=4)

# Analysis
visit_dates = [datetime.fromisoformat(record["visit_date"]).strftime("%Y-%m") for record in medical_records]
visits_per_month = Counter(visit_dates)

print(visits_per_month)