import asyncio
import gspread_asyncio
from google.oauth2.service_account import Credentials

async def write_to_google_sheet():
    # Load credentials from JSON key file
    credentials = Credentials.from_authorized_user_file('key.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create an asyncio client with the credentials
    client = await gspread_asyncio.AsyncioGspreadClientManager(credentials).authorize()

    # Open the spreadsheet by URL or narlme
    sheet = await client.open_by_url('https://docs.google.com/spreadsheets/d/1YHAJFg60sB_Jv-vxfXJutoUvAsip9XqjEuVg0wVbi98/edit?usp=sharing')

    # Select a worksheet for writing
    worksheet = await sheet.get_worksheet(0)

    # Write data
    data = ["Value 1", "Value 2", "Value 3"]
    await worksheet.append_table([data])

# Run the asynchronous function
loop = asyncio.get_event_loop()
loop.run_until_complete(write_to_google_sheet())
