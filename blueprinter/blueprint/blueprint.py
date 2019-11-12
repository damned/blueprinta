import svgwrite

class Blueprint:
    def __init__(self, filename):
        width = 1600
        height = 800
        self._svg = svgwrite.Drawing(filename, profile='tiny', size=(width, height))
        self._svg.add(self._svg.rect((0, 0), (width, height), fill='white'))
        self.gap = 20
        self.card_half_width = 50
        self.card_width = self.card_half_width * 2
        self.card_half_height = 40
        self.card_height = self.card_half_height * 2
        self.lane_count = 0

    def add_lane(self, name):
        group = svgwrite.container.Group()
        self._svg.add(group)
        self.lane_count += 1
        x = self.gap + self.card_half_width
        y = self.lane_count * (self.gap + self.card_height)
        text = self._svg.text(name, insert=(x, y), fill='black', font_family='sans', text_anchor='middle')
        group.add(text)
        return Lane(self._svg, group, self, x, y)

    def save(self):
        self._svg.save()


class Lane:
    def __init__(self, svg, group, config, x, y):
        self._group = group
        self._svg = svg
        self._config = config
        self.x = x
        self.y = y
        self.count = 0

    def add_gap(self):
        self.count += 1

    def add_card(self, name):
        card_group = svgwrite.container.Group()
        self.count += 1
        x = self.x + self.count * (self._config.gap + self._config.card_width)
        y = self.y
        card_group.add(self._svg.rect((x - self._config.card_half_width, y - self._config.card_half_height), (self._config.card_width, self._config.card_height), fill='lightblue'))
        card_group.add(self._svg.text(name, insert=(x, y), fill='black', font_family='sans', text_anchor='middle'))
        self._group.add(card_group)

