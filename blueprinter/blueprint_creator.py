from .blueprint.blueprint import Blueprint
from .sheet.sheet import Sheet

class BlueprintCreator:
    def __init__(self, blueprint_class=Blueprint, sheet_class=Sheet):
        self.blueprint_class = blueprint_class
        self.sheet_class = sheet_class

    def create_blueprint(self, sheet_filename, blueprint_filename):
        blueprint = self.blueprint_class(blueprint_filename)
        sheet = self.sheet_class(sheet_filename)

        for column in sheet.columns:
            lane = blueprint.add_lane(column.cell(0).content)
            for row in range(1, column.row_count):
                lane.add_card(column.cell(row).content)

        blueprint.save()