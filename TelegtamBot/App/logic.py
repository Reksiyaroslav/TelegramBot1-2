import openpyxl


def new_type_sq(file, inform_text):
    worbook = openpyxl.load_workbook(file)
    worksheet = worbook.active
    for row in range(0, worksheet.max_row):
        for col in worksheet.iter_cols(1, worksheet.max_column):
            if col[row].value != "Тема" or col[row].value != "Урок":
                col[row].value = inform_text
            else:
                continue

def new_average_rating_grop(file ):
    pass