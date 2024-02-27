from __future__ import print_function
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle
import webbrowser


SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SPREADSHEET_ID = "1P7_Zoj-wgHUscVoh0-SRl-XEX2rLBkl9mQnAdQs0P0o"

def load_credentials():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", 'w') as token:
            token.write(credentials.to_json())
    return credentials

def batch_update_sheet_cells(sheet, updates):
    data = []
    for cell, value in updates.items():
        data.append({
            "range": f"Sheet1!{cell}",
            "values": [[value]],
        })
    body = {"data": data, "valueInputOption": "RAW"}
    result = sheet.values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
    total_cells_updated = sum([r['updatedCells'] for r in result.get('responses', [])])
    return total_cells_updated

def main(checker):
    with open('dictionary_page0.pkl', 'rb') as file:
        dictionary_page0 = pickle.load(file)
    
    credentials = load_credentials()

    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    
    keys_and_cells = {
            'MSN': 'C10',
            'Engine Type': 'M8:P8',
            'KILO/LIVRE': 'J8:L8',
            'VERSION': 'E10',
            'Part Number': 'H10',
            'Serial Number': 'K10',
            'Stamp': 'M10',
            'Date': 'p10',
            'Left Pump 1 P(bar)': 'E12',
            'Left Pump 2 P(bar)': 'G12',
            'Right Pump 1 P(bar)': 'I12',
            'Right Pump 2 P(bar)': 'K12',
            'Fuel_Density': 'K22',
            'Fuel_Temperature': 'K23',
            'Ambient_Temperature': 'K24',
            'Pitch': 'K26',
            'Roll': 'K27',
            'stp1 volume': 'C17',
            'step1 FOB': 'O17',
            'step1 uplifted': 'E17',
            'step1 left': 'F17',
            'step1 center': 'G17',
            'step1 right': 'H17',
            'stp2 volume': 'C18',
            'step2 FOB': 'O18',
            'step2 uplifted': 'E18',
            'step2 left': 'F18',
            'step2 center': 'G18',
            'step2 right': 'H18',
            'stp3 volume': 'C19',
            'step3 FOB': 'O19',
            'step3 uplifted': 'E19',
            'step3 left': 'F19',
            'step3 center': 'G19',
            'step3 right': 'H19',
            "Jet Pump 1 start mass": 'C24:C25',
            "Jet Pump 1 end mass": 'D24:D25', 
            "Jet Pump 2 start mass": 'C26:C27',
            "Jet Pump 2 end mass": 'D26:D27',
            "Mass Rate 1 (kg/min)": 'E24:E25',
            "Mass Rate 2 (kg/min)": 'E26:E27',
            'RATE': 'F24:F25',
            'Accuracy %': 'P19',
            # Add more keys and cells as needed
        }    
    if checker == 2:
        keys_and_cells['Mass Rate 1 (lb/min)'] = keys_and_cells.pop('Mass Rate 1 (kg/min)')
        keys_and_cells['Mass Rate 2 (lb/min)'] = keys_and_cells.pop('Mass Rate 2 (kg/min)')

    updates = {}

    for key, cell in keys_and_cells.items():
        value_to_export = dictionary_page0.get(key, '')
        updates[cell] = str(value_to_export)

    total_cells_updated = batch_update_sheet_cells(sheet, updates)
    print(f'Total {total_cells_updated} cells updated.')
    
    webbrowser.open(f'https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}')

if __name__ == '__main__':
    main()
