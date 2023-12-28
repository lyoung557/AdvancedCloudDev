#Import libraries
import json
from faker import Faker

#Function for generating a profile using faker
def generate_user_profile():
    fake = Faker()
    profile = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'birthdate': fake.date_of_birth().strftime('%Y-%m-%d')
    }
    return profile

#Function for calling generate_user_profile() the number of times specified in range
def generate_user_profiles(num_profiles):
    profiles = [generate_user_profile() for _ in range(num_profiles)]
    return profiles

#Function for creating JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

#Function to read JSON file
def read_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

#Function to filter by birth year (ex 3)
def filter_profiles_by_birth_year(profiles, year_threshold):
    filtered_profiles = [profile for profile in profiles if int(profile['birthdate'][:4]) > year_threshold]
    return filtered_profiles

#Function to set the key of the data to email
def transform_data_by_email(profiles):
    transformed_data = {profile['email']: profile for profile in profiles}
    return transformed_data

# Exercise 1: Generate and store user profiles
user_profiles = generate_user_profiles(10)
save_to_json(user_profiles, 'sg_user_profiles.json')

# Exercise 2: Filter user profiles by birth year
read_profiles = read_from_json('sg_user_profiles.json')
filtered_profiles = filter_profiles_by_birth_year(read_profiles, 1990)
save_to_json(filtered_profiles, 'sg_filtered_profiles.json')

# Exercise 3: Transform data by keying profiles by email address
transformed_data = transform_data_by_email(read_profiles)
save_to_json(transformed_data, 'sg_transformed_profiles.json')
