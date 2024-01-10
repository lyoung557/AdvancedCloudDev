import json

with open('user_profiles.json', 'r') as file:
    profiles = json.load(file)

transformed_data = {profile['email']: profile for profile in profiles}

with open('transformed_profiles.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)
