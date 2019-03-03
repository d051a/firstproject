import xlrd


class ExcelParser():
    def parse(self, filename):
        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)
        result = {}
        for row in range(sh.nrows):
            line = sh.cell_value(rowx=row, colx=1)
            result[sh.cell_value(rowx=row, colx=0)] = line.replace(u'\xa0', ' ')
        return result
