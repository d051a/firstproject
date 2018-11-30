import xlrd

# book = xlrd.open_workbook("book1.xlsx")
# print("The number of worksheets is {0}".format(book.nsheets))
# print("Worksheet name(s): {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
# print("Cell D30 is {0}".format(sh.cell_value(rowx=11, colx=1)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))


class ExcelParser(object):

    def parse(self, filename):
        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)
        result = {}
        for row in range(sh.nrows):
            line = sh.cell_value(rowx=row, colx=1)
            result[sh.cell_value(rowx=row, colx=0)] = line.replace(u'\xa0', ' ')
        return result
