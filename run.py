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

def get_name_data():
    """
    Get name input from the user 
    """ 
    while True: 
        print("What is your name and surname?") 
        print("Your name should be in alphabetical letters") 
        print("Example: Jon Bloggs\n") 
        
        name = input("Enter your name here:\n") 
        
        valid_name = name_data.title() 
        
        if validate_data(name_data): 
            print("Name entry is accepted") 
            break 

def validate_data(name): 
    valid_name = name_data.title()
    validate_data(name_data) 
    """ 
    Inside the try, converts all first letters of name and surname 
    into capital letters. Raises ValueError if the letters entered are 
    all lowercase. 
    """ 
    try: 
        [name_data for name in valid_name]
        if name_data != valid_name: 
            raise ValueError( 
                f"First letter of Name and Surname should be capital letters" 
                ) 
    except ValueError as e:
        print(f"Case sensitive: {e}, please retry.")
    return False 

    return True

def update_account_worksheet(accounts):
 """
 Update account worklist, adding a new account to the list provided
 """ 
 print("Updating accounts worksheet ...\n") 
 accounts_worksheet = SHEET.worksheet("accounts")
 accounts_worksheet.append_row(accounts)
 print("Accounts worksheet updated successfully.\n")

def update_worksheet(accounts, worksheet):
 """
 Updates the relevant worksheet with the data provided
 """
 print(f"Updating (worksheet) worksheet ...\n") 
 worksheet_to_update = SHEET.worksheet(worksheet)  
 worksheet_to_update.append_row(accounts)
 print(f"{worksheet} worksheet updated successfully\n")

def update_account_holders_type_worksheet(account_holders_data):
 """
 Update account holders type worksheet, adding a new account to the list provided
 """
 print("Updating account holders type worksheet ...\n") 
 account_holders_type_worksheet = SHEET.worksheet("account_holder_type")
 account_holders_type_worksheet.append_row(account_holders_type)
 print("Accounts holders type worksheet updated successfully.\n")

def name_account_type_data(name_A1, A12):
 """
 Get the names and account types of all customers at Argon Bank
 """
 print("Getting data request ...\n")
 account_type = SHEET.worksheet(account_type).get_all_values()
 accounts_type_row = accounts(E1,E12) 
 
 account_holders_data = []
 for account_type, name in zip(account_type_row(E1, E12), name_row(A1, A12)):
    account_holders = name + account_type
 account_holders_data.append(account_holders_data)


def main():
 """
 Run all programs
 """ 
 run.get_name_data() 
 run.update_account_worksheet(name_data, accounts)
 name_account_type(accounts)
 update_worksheet(account_holders_data, name)

print("Welcome to Argon Bank Data Automation")
main()

