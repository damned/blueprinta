import pytest
import datetime
import os.path

from .buildable_sheet_builder import BuildableSheetBuilder
from ..blueprinter.blueprint_creator import BlueprintCreator
from .blueprint_reader import parse_blueprint

@pytest.fixture
def sheetfile():
    return f'build/tmp{int(datetime.datetime.now().timestamp())}.xlsx'

def setup():
    os.makedirs('build', exist_ok=True)

def test_creates_cards_in_lanes_from_cells(sheetfile):
    sheet = sheet_builder(sheetfile).with_rows(
        ['lane heading 1', 'lane heading 2'], 
        ['card 1a', 'card 2a'],
        ['card 1b', 'card 2b']).build()
    
    blueprint_filename = sheet.basepath + '.svg'
    create_blueprint(sheet.filename, blueprint_filename)

    blueprint = parse_blueprint(blueprint_filename)

    assert blueprint.lanes == ['lane heading 1', 'lane heading 2']
    assert blueprint.cards == ['card 1a', 'card 1b', 'card 2a', 'card 2b']


def sheet_builder(sheetfile):
    return BuildableSheetBuilder(sheetfile)


def create_blueprint(sheet_filename, blueprint_filename):
    print(blueprint_filename)
    BlueprintCreator().create_blueprint(sheet_filename, blueprint_filename)

    