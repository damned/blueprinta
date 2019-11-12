from .blueprint.blueprint import Blueprint
from .sheet.sheet import Sheet

class BlueprintCreator:
    def __init__(self, blueprint_class=Blueprint, sheet_class=Sheet):
        self.blueprint_class = blueprint_class
        self.sheet_class = sheet_class

    def create_blueprint(self, sheet_filename, blueprint_filename):
        blueprint = self.blueprint_class(blueprint_filename)
        sheet = self.sheet_class(sheet_filename)

        heading_row = 0
        print(sheet.cell_note(0, 0))
        if sheet.cell_note(0, 0) == 'skip':
            heading_row = 1
        for column in sheet.columns:
            lane = blueprint.add_lane(column.cell(heading_row).content)
            for row in range(heading_row + 1, column.row_count):
                content = column.cell(row).content
                if content:
                    lane.add_card(column.cell(row).content)
                else:
                    lane.add_gap()

        blueprint.save()