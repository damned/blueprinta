import svgwrite

class Blueprint:
    def __init__(self, filename):
        self._svg = svgwrite.Drawing(filename, profile='tiny', size=(800, 600))

    def add_lane(self, name):
        group = svgwrite.container.Group()
        self._svg.add(group)
        return Lane(self._svg, group)


    def save(self):
        self._svg.save()


class Lane:
    def __init__(self, svg, group):
        self._group = group
        self._svg = svg

    def add_card(self, name):
        self._group.add(self._svg.rect((0, 0), (100, 80), fill='lightblue'))


