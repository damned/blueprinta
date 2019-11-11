from openpyxl import load_workbook

class Sheet:
    def __init__(self, filename):
        self._workbook = load_workbook(filename)

    @property
    def _sheet(self):
        return self._workbook.active

    @property
    def columns(self):
        cols = []
        for col_index in range(self._sheet.min_column, self._sheet.max_column + 1):
            column = Column()
            cols.append(column)
            for row_index in range(self._sheet.min_row, self._sheet.max_row + 1):
                column.add_cell(self._sheet.cell(row=row_index, column=col_index))

        return cols


class Column:
    def __init__(self):
        self._cells = []

    def add_cell(self, excel_cell):
        self._cells.append(Cell(excel_cell))

    def cell(self, index):
        print(self._cells)
        print(len(self._cells))
        return self._cells[index]


class Cell:
    def __init__(self, cell):
        self._cell = cell

    @property
    def content(self):
        return self._cell.value
