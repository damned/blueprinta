from .blueprint.blueprint import Blueprint
from .sheet.sheet import Sheet
from .blueprint_creator import BlueprintCreator

class FileBasedBlueprintCreator:
    def create_blueprint(self, sheet_filename, blueprint_filename):
        sheet = Sheet(sheet_filename)
        blueprint = Blueprint(blueprint_filename)

        BlueprintCreator().create_blueprint(sheet, blueprint)