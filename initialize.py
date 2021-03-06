from xlrd import open_workbook

class BookingReview(object):
    def __init__(self, company, id, rate, context, post_time, spam_ham,
                 context_backup):
        self.company = company
        self.id = id
        self.rate = rate
        self.context = context
        self.post_time = post_time
        self.spam_ham = spam_ham
        self.context_backup = context_backup

    def __str__(self):
        return ("BookingReview object:\n"
                "  Company name = {0}\n"
                "  ID = {1}\n"
                "  Rating = {2}\n"
                "  Current Context = {3}\n"
                "  Post time = {4}\n"
                "  Spam/Ham = {5}\n"
                "  Original Context = {6}\n"
                .format(self.company, self.id, self.rate,
                        self.context, self.post_time, self.spam_ham,
                        self.context_backup))
    def change(self):
        self.rate = 100

def xl_to_BookingReview(file_dir):
    wb = open_workbook(file_dir)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        items = []

        rows = []
        # 모든 데이터 처리를 원할 경우 -> range(1, number_of_rows)
        for row in range(1, 6):
            values = []
            values.append(str(sheet.cell(row,0).value))
            values.append(str(sheet.cell(row,1).value))
            values.append(int(sheet.cell(row,2).value))
            values.append(str(sheet.cell(row,3).value))
            values.append(str(sheet.cell(row,4).value))
            values.append(bool(sheet.cell(row,5).value))
            values.append(str(sheet.cell(row,3).value))
            
            item = BookingReview(*values)
            items.append(item)

    return items

