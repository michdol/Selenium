import xlrd


file_location = "./users.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(1, sheet.nrows)]



def excel_get_email(name):
    for i in data:
        if name == i[1]:
            return i[3]


def excel_get_password(name):
    for i in data:
        if name == i[1]:
            return i[4]
