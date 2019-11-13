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
        print(sheet.cell_colour(0, 0))
        if sheet.cell_note(0, 0) == 'skip':
            heading_row = 1
        for column in sheet.columns:
            heading = column.cell(heading_row)
            if not heading.content:
                continue

            print(heading.colour)
            print(heading.content)
            lane = blueprint.add_lane(heading.content, colour=heading.colour)
            for row in range(heading_row + 1, column.row_count):
                cell = column.cell(row)
                content = cell.content
                if content and content != '"':
                    lane.add_card(column.cell(row).content, colour=cell.colour)
                else:
                    lane.add_gap()

        blueprint.save()