from .sheet import Sheet

class SheetBuilder:
    def __init__(self, filename):
        self.sheet = Sheet(filename)

    def with_rows(self, *rows):
        for row in rows:
            self.sheet.add_row(*row)
        return self

    def build(self):
        self.sheet.save()
        return self.sheet