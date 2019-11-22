import pytest

from blueprinter.blueprint_creator import BlueprintCreator


@pytest.fixture
def blueprint():
    return FakeBlueprint()

@pytest.fixture
def sheet():
    return FakeSpreadsheet()

def test_adds_lane_for_first_cell(blueprint, sheet):
    creator = BlueprintCreator()

    sheet.add_cell_to_next_row('a lane')

    creator.create_blueprint(sheet, blueprint)

    assert blueprint.lane_names == ['a lane']


class FakeBlueprint:
    def __init__(self):
        self._lanes = []

    def add_lane(self, name, colour=None):
        self._lanes.append(self.FakeLane(name, colour))

    def save(self):
        pass

    @property
    def lane_names(self):
        return [lane.name for lane in self._lanes]

    class FakeLane:
        def __init__(self, name, colour=None):
            self.name = name

class FakeSpreadsheet:
    def __init__(self):
        self._notes = dict()
        self._columns = [self.FakeColumn()]

    def add_cell_to_next_row(self, text):
        self._column.add_cell(text)

    @property
    def _column(self):
        return self._columns[-1] 

    def cell_note(self, col, row):
        return self._notes.get((col, row))

    def cell_colour(self, col, row):
        return None

    @property
    def columns(self):
        return self._columns

    class FakeColumn:
        def __init__(self):
            self._cells = []

        def cell(self, row):
            return self._cells[row]

        def add_cell(self, text):
            self._cells.append(self.FakeCell(text))

        @property
        def row_count(self):
            return len(self._cells)

        class FakeCell:
            def __init__(self, text):
                self.content = text
                self.colour = None
