import svgwrite



class BlueprintCreator:
    def __init__(self):
        pass

    def create_blueprint(self, sheet_filename, blueprint_filename):

        svg = svgwrite.Drawing(blueprint_filename, profile='tiny', size=(800, 600))

        group = svgwrite.container.Group()
        svg.add(group)

        group.add(svg.rect((0, 0), (100, 80), fill='lightblue'))
        svg.save()