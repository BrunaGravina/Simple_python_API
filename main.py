from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        if restaurant is None:
            return {'Data': json_data}

        data_restaurant = []
        for item in json_data:
            if item['Company'] == restaurant:
                data_restaurant.append({'item': item['Item'],
                                                         'price': item['price'],
                                                         'description': item['description']})
        return {'Restaurant': restaurant, 'Menu': data_restaurant}
    else:
        return{'Erro': f'{response.status_code} - {response.text}'}
