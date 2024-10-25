import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    json_data = response.json()
    data_restaurant = {}
    for item in json_data:
        restaurant_name = item ['Company']
        if restaurant_name not in data_restaurant:
            data_restaurant[restaurant_name] = []
        data_restaurant[restaurant_name].append({'item': item['Item'],
                                                 'price': item['price'],
                                                 'description': item['description']})

else:
    print(f'Error code: {response.status_code}')

for restaurant_name, data in data_restaurant.items():
    file_name = f'{restaurant_name}.json'
    with open(file_name, 'w') as restaurant_file:
        json.dump(data, restaurant_file, indent=4)