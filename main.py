from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_search import FlightSearch

TWILIO_ACC_SID = "AC4998de1745722ffbed33028f9cae7aa7"
TWILIO_AUTH_TOKEN = "846f6810b44bfbb3dbeaee3f9626c127"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# if sheet_data[0]["iataCode"] == "":
#     from flight_search import FlightSearch
#     flight_search = FlightSearch()
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     pprint(f"sheet_data:\n {sheet_data}")
#
# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
#
# for destination in sheet_data:
#     flight = flight_search.check_flights(
#         origin_city_code="LON",
#         destination_city_code=destination["iataCode"],
#         from_time=tomorrow,
#         to_time=six_month_from_today
#     )






data_manager.destination_data = sheet_data
data_manager.update_destination_codes()