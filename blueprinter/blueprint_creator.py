from.blueprint.blueprint import Blueprint

class BlueprintCreator:
    def __init__(self, blueprint_class=Blueprint):
        self.blueprint_class = blueprint_class

    def create_blueprint(self, sheet_filename, blueprint_filename):
        blueprint = self.blueprint_class(blueprint_filename)
        lane = blueprint.add_lane('lane')
        lane.add_card('card')

        blueprint.save()