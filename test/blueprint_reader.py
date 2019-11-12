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
    def _top_nodes(self):
        return self._dom.getElementsByTagName('svg')[0].childNodes

    @property
    def groups(self):
        return [child for child in self._top_nodes if child.tagName == 'g']


class Blueprint:
    def __init__(self, svg):
        self._svg = svg

    @property
    def cards(self):
        cards = []
        for lane in self._lanes:
            for card in lane.cards:
                cards.append(card.name)
        
        return cards

    @property
    def card_positions(self):
        positions = []
        for lane in self._lanes:
            for card in lane.cards:
                positions.append(card.position)
        
        return positions


    @property
    def lane_positions(self):
        return [lane.position for lane in self._lanes]

    @property
    def lanes(self):
        return [lane.name for lane in self._lanes]

    @property
    def _lanes(self):
        return [Lane(group) for group in self._svg.groups]
    

def text_node_text(node):
    return node.childNodes[0].nodeValue

def text_node_position(node):
    return (int(node.getAttribute('x')), int(node.getAttribute('y')))

def text_content(svg_element):
    return text_node_text(svg_element.getElementsByTagName('text')[0])

def text_position(svg_element):
    return text_node_position(svg_element.getElementsByTagName('text')[0])


class Lane:
    def __init__(self, group):
        self._group = group

    @property
    def name(self):
        return text_content(self._group)

    @property
    def position(self):
        return text_position(self._group)

    @property
    def cards(self):
        return [Card(card_group) for card_group in self._group.getElementsByTagName('g')]


class Card:
    def __init__(self, group):
        self._group = group

    @property
    def name(self):
        return text_content(self._group)

    @property
    def position(self):
        return text_position(self._group)


