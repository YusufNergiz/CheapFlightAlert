import os

import requests
from flight_data import FlightData
from dotenv import load_dotenv
load_dotenv()
FLIGHT_SEARCH_API = os.getenv("FLIGHT_SEARCH_API")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": FLIGHT_SEARCH_API}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": FLIGHT_SEARCH_API}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "curr": "USD"
        }

        response_from_flights = requests.get(url=location_endpoint, headers=headers, params=query)

        try:
            data = response_from_flights.json()['data'][0]
        except IndexError:
            print(f"No Flights Found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            destination_city=data["cityTo"],
            origin_airport=data["flyFrom"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: $ {flight_data.price}")
        return flight_data







# iata_code_finder = {
#     "apikey": FLIGHT_SEARCH_API,
#     "term": city_name,
#     "location_types": "city"
# }
#
# request = requests.get("https://tequila-api.kiwi.com", headers=iata_code_finder)
# destination_code_data = request.json()
# print(destination_code_data.text)
# code = destination_code_data["locations"][0]["code"]
# return code


####  I wes last stuck here the "locations" inside code = destination_code_data isnt found which is from the example in the Tequilia site.
