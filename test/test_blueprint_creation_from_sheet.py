import pytest
import datetime
import os.path

from .sheet_builder import SheetBuilder
from ..blueprinter.blueprint_creator import BlueprintCreator
from .blueprint_reader import parse_blueprint

@pytest.fixture
def sheetfile():
    return f'build/tmp{int(datetime.datetime.now().timestamp())}.xslx'

def setup():
    os.makedirs('build', exist_ok=True)

def test_creates_card_from_cell(sheetfile):
    sheet = sheet_builder(sheetfile).with_rows(['lane heading 1'], ['card 1']).build()
    
    blueprint_filename = sheet.basepath + '.svg'
    create_blueprint(sheet.filename, blueprint_filename)

    blueprint = parse_blueprint(blueprint_filename)

    assert blueprint.lanes == ['lane heading 1']
    assert blueprint.cards == ['card 1']


def sheet_builder(sheetfile):
    return SheetBuilder(sheetfile)


def create_blueprint(sheet_filename, blueprint_filename):
    BlueprintCreator().create_blueprint(sheet_filename, blueprint_filename)

    