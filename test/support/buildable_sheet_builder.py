from .buildable_sheet import BuildableSheet

class BuildableSheetBuilder:
    def __init__(self, filename):
        self.sheet = BuildableSheet(filename)

    def with_rows(self, *rows):
        for row in rows:
            self.sheet.add_row(*row)
        return self

    def build(self):
        self.sheet.save()
        return self.sheet