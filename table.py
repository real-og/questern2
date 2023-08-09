import gspread
from loader import SHEET_LINK

class WorkSheet:
    def __init__(self, link: str):
        self.link = link
        self.account = gspread.service_account(filename='key.json')
        self.sheet = self.account.open_by_url(self.link).sheet1

    def append_user(self, id: str, username: str, full_name: str = 'Без имени'):
        cell = self.sheet.find(id)
        if cell is None:
            self.sheet.append_row([id, username, full_name, '1'])
        else:
            self.sheet.update_cell(cell.row, 4, '1')

        
    def change_level(self, id, level):
        cell = self.sheet.find(id)
        if cell is None:
            return
        row_number = cell.row
        self.sheet.update_cell(row_number, 4, level)

    def change_name(self, id, name):
        cell = self.sheet.find(id)
        if cell is None:
            return
        row_number = cell.row
        self.sheet.update_cell(row_number, 5, name)

    def change_email(self, id, email):
        cell = self.sheet.find(id)
        if cell is None:
            return
        row_number = cell.row
        self.sheet.update_cell(row_number, 6, email)

    def set_lottary_number(self, id, number):
        cell = self.sheet.find(id)
        if cell is None:
            return
        row_number = cell.row
        self.sheet.update_cell(row_number, 7, number)


sheet = WorkSheet(SHEET_LINK)