from.blueprint.blueprint import Blueprint

class BlueprintCreator:
    def __init__(self):
        pass

    def create_blueprint(self, sheet_filename, blueprint_filename):
        blueprint = Blueprint(blueprint_filename)
        blueprint.save()