import svgwrite

def hex_to_svg_rgb_string(hex, default='white'):
    if not hex:
        return default
    return 'rgb' + str(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))

class Blueprint:
    def __init__(self, filename):
        self.width = 1600
        height = 900
        self.full_width_elements = []
        self._svg = svgwrite.Drawing(filename, profile='tiny', size=(self.width, height))
        background = self._svg.rect((0, 0), (self.width, height), fill='white')
        self._svg.add(background)
        self.full_width(self._svg, background)
        self.gap = 20
        self.card_half_width = 50
        self.card_width = self.card_half_width * 2
        self.card_half_height = 40
        self.card_height = self.card_half_height * 2
        self.lane_count = 0
        self.line_spacing = 14
        self.lanes = []

    def full_width(self, *elements):
        self.full_width_elements += elements

    def update_full_width(self, width):
        for e in self.full_width_elements:
            e['width'] = width

    def add_lane(self, name, colour=None):
        group = svgwrite.container.Group()
        self._svg.add(group)
        self.lane_count += 1
        x = self.gap + self.card_half_width
        y = self.lane_count * (self.gap + self.card_height)
        lane_background = self._svg.rect((0, y - (self.gap + self.card_height) / 2), (self.width, self.card_height + self.gap), fill=hex_to_svg_rgb_string(colour))
        group.add(lane_background)
        text = self._svg.text(name, insert=(x, y), fill='black', font_family='sans', text_anchor='middle')
        group.add(text)
        lane = Lane(self._svg, group, self, x, y)
        self.full_width(lane_background)
        self.lanes.append(lane)
        return lane

    def max_card_extent_in_x(self):
        max_x = 0
        for lane in self.lanes:
            max_x = max(max_x, lane.max_x)
        return max_x

    def save(self):
        self.update_full_width(self.max_card_extent_in_x() + self.gap)
        self._svg.save()


class Lane:
    def __init__(self, svg, group, config, x, y):
        self._group = group
        self._svg = svg
        self._config = config
        self.x = x
        self.y = y
        self.count = 0
        self.max_x = 0

    def add_gap(self):
        self.count += 1

    def add_card(self, name, colour=None):
        config = self._config
        card_group = svgwrite.container.Group()
        self.count += 1
        x = self.x + self.count * (config.gap + config.card_width)
        y = self.y
        self.max_x =max(self.max_x, x + config.card_half_width)
        card_group.add(self._svg.rect((x - config.card_half_width, y - config.card_half_height), (config.card_width, config.card_height), fill=hex_to_svg_rgb_string(colour, 'white')))
        main_text = name.split('\n')[0]
        lines = main_text.split(' ')
        line_offset = -config.line_spacing * (len(lines) - 1) / 2.0
        for line in lines:
            card_group.add(self._svg.text(line, insert=(x, y + line_offset), fill='black', font_family='sans', text_anchor='middle'))
            line_offset += config.line_spacing

        self._group.add(card_group)

