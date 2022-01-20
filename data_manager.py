import requests

SHEETY_API = "https://api.sheety.co/c5d2d6073671790affbecf328afa0a7e/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_API)
        google_sheets_data = response.json()
        self.destination_data = google_sheets_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{SHEETY_API}/{city['id']}", json=new_data)



