import svgwrite

class Blueprint:
    def __init__(self, filename):
        self._svg = svgwrite.Drawing(filename, profile='tiny', size=(800, 600))
        self.gap = 10
        self.card_half_width = 50
        self.card_width = self.card_half_width * 2

    def add_lane(self, name):
        group = svgwrite.container.Group()
        self._svg.add(group)
        x = self.gap + self.card_half_width
        y = 25
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
        self.card_count = 0

    def add_card(self, name):
        card_group = svgwrite.container.Group()
        self.card_count += 1
        x = self.x + self.card_count * (self._config.gap + self._config.card_width)

        card_group.add(self._svg.rect((x - self._config.card_half_width, 0), (self._config.card_width, 80), fill='lightblue'))
        card_group.add(self._svg.text(name, insert=(x, 25), fill='black', font_family='sans', text_anchor='middle'))
        self._group.add(card_group)

