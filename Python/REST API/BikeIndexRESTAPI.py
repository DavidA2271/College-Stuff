import requests
import json

class Bike_Response:
    ''' Handles the requests and json operations '''
    site = 'https://bikeindex.org:443/api/v3/search?'
    def __init__(self, params) -> None:
        self.params = params
    def query(self):
        ''' requests bike info '''
        url = self.site + str(self.params)
        response = requests.get(url)
        print(f'Getting {int(self.params.pages)*int(self.params.per_page)} bikes')
        self.json_response = response.json()
        self.bikes = self.json_response['bikes']
        print(f'Received {len(self.bikes)} bikes')
    def get_images(self):
        ''' requests images of bikes from first query '''
        self.bike_imgs = []
        print(f'Getting {len(self.bikes)} images')
        for bike in self.bikes:
            if bike['large_img'] is not None:
                self.bike_imgs.append((bike['id'], bike['large_img']))
        print(f'Received {len(self.bike_imgs)} images')
    def save_data(self):
        ''' saves bike info to json and bike pictures to png '''
        json_object = json.dumps(self.json_response['bikes'], indent=4)
        with open('bikes.json', 'w') as handle:
            handle.write(json_object)
        for id,img_url in self.bike_imgs:
            img = requests.get(img_url, stream=True)
            if img.status_code == 200:
                with open(f'{id}.png', 'wb') as handle:
                    for chunk in img:
                        handle.write(chunk)
        


class Search_Params:
    ''' Holds parameters for the bike search '''
    def __init__(self, pages='1', per_page='10', serial='', query='', 
                 manufacturer='', colors='', location='New York, NY', distance='10', stolenness='proximity') -> None:
        self.pages = pages.strip()
        self.per_page = per_page.strip()
        self.serial = serial.strip()
        self.query = query.strip()
        self.manufacturer = manufacturer.strip()
        self.colors = colors.strip()
        self.location = location.strip()
        self.distance = distance.strip()
        self.stolenness = stolenness.strip()
    def __str__(self) -> str:
        ''' Converts params to a format that can be used in a url '''
        params = ''
        params = params + f'page={self.pages}'
        params = params + f'&per_page={self.per_page}'
        if self.serial != '':
            params = params + f'&serial={self.serial}'
        if self.query != '':
            query = self.query.replace(' ', '%20')
            query = query.replace(',', '%2C')
            params = params + f'&query={query}'
        if self.manufacturer != '':
            params = params + f'&manufacturer={self.manufacturer}'
        if self.colors != '':
            colors = self.colors
            colors = colors.replace(' ', '%20')
            colors = colors.replace(',', '%2C')
            params = params + f'&colors={colors}'
        if self.location != '':
            location = self.location
            location = location.replace(' ', '%20')
            location = location.replace(',', '%2C')
            params = params + f'&location={location}'
        if self.distance != '':
            params = params + f'&distance={self.distance}'
        if self.stolenness != '':
            params = params + f'&stolenness={self.stolenness}'
        return params

