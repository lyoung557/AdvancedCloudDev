import csv
import requests


# Function to initiate a search on the Intelligence X API
def intelx_search(email, api_key, base_url):
    search_endpoint = f"{base_url}/intelligent/search"
    headers = {"x-key": api_key}
    data = {"term": email, "maxresults": 5}

    response = requests.post(search_endpoint, headers=headers, json=data)
    print("Request URL:", response.request.url)
    print("Response Status Code:", response.status_code)
    if response.status_code == 200:
        return response.json()['id']  # Return the search ID for later use
    else:
        return None


# Function to retrieve the results of a search from the Intelligence X API
def intelx_get_results(search_id, api_key, base_url):
    result_endpoint = f"{base_url}/intelligent/search/result"
    headers = {"x-key": api_key}
    params = {"id": search_id}

    response = requests.get(result_endpoint, headers=headers, params=params)
    print("Request URL:", response.request.url)
    print("Response Status Code:", response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Read email addresses from an input CSV file
def read_emails(input_file_path):
    with open(input_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        emails = [row[0] for row in reader]  # Assuming emails are in the first column
    return emails


# Write the breach check results to an output CSV file
def write_results(output_file_path, results):
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['email_address', 'breached', 'site_where_breached']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


# Main function to check the breach status of each email
def check_emails(input_file_path, output_file_path, api_key, base_url):
    emails = read_emails(input_file_path)
    results = []
    for email in emails:
        search_id = intelx_search(email, api_key, base_url)
        if search_id:
            search_results = intelx_get_results(search_id, api_key, base_url)
            if search_results and search_results['records']:
                # Extract the site names where the breaches occurred
                sites_breached = [record['name'] for record in search_results['records']]
                results.append({
                    'email_address': email,
                    'breached': True,
                    'site_where_breached': '; '.join(sites_breached)  # Join multiple sites with a semicolon
                })
            else:
                results.append({
                    'email_address': email,
                    'breached': False,
                    'site_where_breached': 'None'
                })
        else:
            results.append({
                'email_address': email,
                'breached': 'Error',
                'site_where_breached': 'Error'
            })

    write_results(output_file_path, results)


if __name__ == '__main__':
    api_key = 'ca611a1e-2c47-404a-ad9d-67e8a7b15468'  # Replace with your actual Intelligence X API key
    base_url = 'https://2.intelx.io'  # Replace with the base URL provided by Intelligence X
    input_file_path = 'email_list.csv'  # Replace with the path to your input CSV file containing the email addresses
    output_file_path = 'output_result.csv'  # Replace with the path where you want the output CSV file to be saved

    # Run the check
