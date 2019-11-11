import os

import openpyxl

from openpyxl import Workbook

class Sheet:
    def __init__(self, filename):
        self.filename = filename
        self._wb = Workbook()
    
    @property
    def _sheet(self):
        return self._wb.active

    def add_row(self, *cells):
        self._sheet.append(cells)

    def save(self):
        self._wb.save(self.filename)

    @property
    def basepath(self):
        return os.path.splitext(self.filename)[0]

