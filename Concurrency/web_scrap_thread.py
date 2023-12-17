import threading
import requests

def fetch_url(url):
    print(f'Starting to fetch {url}')
    response = requests.get(url)
    print((f'Finished fetching {url} Status code {response.status_code}'))

urls = ['https://samueladebayo.com', 'https://www.belfastmet.ac.uk/', 'https://github.com/exponentialR/3DCNN']


threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()

print(f'All URLs fetched!')

