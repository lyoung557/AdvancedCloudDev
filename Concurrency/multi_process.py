from multiprocessing import Pool

def process_data(data):
    return data * data

data = [1, 2, 3, 4, 5, 6]

with Pool(4) as p:
    results = p.map(process_data, data)
print(f'Processed data: ', results)
