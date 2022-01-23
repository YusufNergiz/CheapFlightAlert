from googleapiclient import discovery
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHIT_ID = "1ouBe8Mr9edXiXWN5T1r5X66BxqtuiZWSynZ4ziIqEZc"
HTTP_REQUEST = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHIT_ID}/values/A1:C10"
credantials = "AIzaSyAKI76FaPsjP2HadsSByYB1qUI9EsSEjuQ"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open(r"Flight Deals").sheet1


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        service = discovery.build('sheets', 'v4', credentials=credantials)
        request = service.spreadsheets().values().get(spreadsheetId=SPREADSHIT_ID, range="A1:C10")
        response = request.execute()
        # google_sheets_data = response.json()
        # print(google_sheets_data)
        # self.destination_data = google_sheets_data["prices"]
        # return self.destination_data
        pprint(response)

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            # response = requests.put(f"{SHEETY_API}/{city['id']}", json=new_data)



