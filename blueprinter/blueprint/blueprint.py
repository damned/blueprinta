import svgwrite

class Blueprint:
    def __init__(self, filename):
        self.filename = filename

    def save(self):
        svg = svgwrite.Drawing(self.filename, profile='tiny', size=(800, 600))

        group = svgwrite.container.Group()
        svg.add(group)

        group.add(svg.rect((0, 0), (100, 80), fill='lightblue'))
        svg.save()
