import pytest
import datetime
import os.path

from ..blueprinter.blueprint.blueprint import Blueprint
from .blueprint_reader import parse_blueprint

@pytest.fixture
def blueprint_filename():
    return f'build/tmp{datetime.datetime.now().timestamp()}.svg'

def setup():
    os.makedirs('build', exist_ok=True)

def test_lays_out_cards_along_lane(blueprint_filename):
    blueprint = Blueprint(blueprint_filename)

    lane = blueprint.add_lane('laney')
    lane.add_card('cardi a')
    lane.add_card('cardi b')
    blueprint.save()

    actual_blueprint = parse_blueprint(blueprint_filename)

    assert actual_blueprint.lanes == ['laney']
    
    lane_x, lane_y = actual_blueprint.lane_positions[0]
    assert lane_x == blueprint.gap + blueprint.card_half_width

    assert actual_blueprint.card_positions[0][1] == lane_y
    assert actual_blueprint.card_positions[1][1] == lane_y

    assert actual_blueprint.card_positions[0][0] == lane_x + blueprint.gap + blueprint.card_width
    assert actual_blueprint.card_positions[1][0] == lane_x + 2 * blueprint.gap + 2 * blueprint.card_width


    