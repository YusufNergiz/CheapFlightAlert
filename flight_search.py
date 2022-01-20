import requests
FLIGHT_SEARCH_API = "yLyVv9M6e-7EkLGdfpw56LUfzRwTyzMN"
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

    def get_destination_price(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": FLIGHT_SEARCH_API}

        query = {
            "fly_from": "LON",
            "fly_to": self.get_destination_code(city_name),
            "date_from": 1/20/2022,
            "date_to": 7/20/2022,
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()
        return results

    



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
