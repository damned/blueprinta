from xml.dom import minidom

def parse_blueprint(filename):
    svg = parse_svg(filename)
    return Blueprint(svg)


def parse_svg(filename):
    dom = minidom.parse(filename)
    return Svg(dom)
    

class Svg:
    def __init__(self, dom):
        self._dom = dom

    @property
    def groups(self):
        return self._dom.getElementsByTagName('g')


class Blueprint:
    def __init__(self, svg):
        self._svg = svg

    @property
    def cards(self):
        cards = []
        for lane in self._lanes:
            cards += lane.cards
        return cards

    @property
    def lanes(self):
        return [lane.name for lane in self._lanes]

    @property
    def _lanes(self):
        return [Lane(group) for group in self._svg.groups]
    

class Lane:
    def __init__(self, group):
        self._group = group

    @property
    def name(self):
        return 'lane heading 1'

    @property
    def cards(self):
        return ['card 1' for rect in self._group.getElementsByTagName('rect')]

