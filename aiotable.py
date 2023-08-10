import gspread_asyncio
from google.oauth2.service_account import Credentials
from loader import SHEET_LINK

link = SHEET_LINK
def get_creds():
    creds = Credentials.from_service_account_file("key.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
async def get_sheet(agcm=agcm):
    agc = await agcm.authorize()
    ss = await agc.open_by_url(link)
    zero_ws = await ss.get_worksheet(0)
    return zero_ws

async def append_user(id: str, username: str, full_name: str = 'Без имени'):
        sheet = await get_sheet()
        cell = await sheet.find(id)
        if cell is None:
            await sheet.append_row([id, username, full_name, '1'])
        else:
            await sheet.update_cell(cell.row, 4, '1')

async def change_level(id, level):
    sheet = await get_sheet()
    cell = await sheet.find(id)
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, 4, level)

async def change_name(id, name):
    sheet = await get_sheet()
    cell = await sheet.find(id)
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, 5, name)

async def change_email(id, email):
    sheet = await get_sheet()
    cell = await sheet.find(id)
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, 6, email)

async def set_lottary_number(id, number):
    sheet = await get_sheet()
    cell = await sheet.find(id)
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, 7, number)



