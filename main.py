import flight_search
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint


TWILIO_ACC_SID = "AC4998de1745722ffbed33028f9cae7aa7"
TWILIO_AUTH_TOKEN = "846f6810b44bfbb3dbeaee3f9626c127"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     pprint(f"sheet_data:\n {sheet_data}")

flight_search = FlightSearch()
flight_search.get_destination_price("Paris")




data_manager.destination_data = sheet_data
data_manager.update_destination_codes()