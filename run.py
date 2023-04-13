import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')  
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('argon-bank')

def get_username_data():
    """
    Get username name input from the user
    """

    print("What is your username")
    print("Your username should be an email")
    print("Example:j.bloggs@yahoo.com\n")

    data = input("Enter your username here:")
    print(f"The data provided is {data}")

get_username_data()    




