import pytest

from blueprinter.blueprint.text_splitter import TextSplitter

splitter = TextSplitter()

def test_splits_uneven_words():
    lines = splitter.split('I want bubbles')

    assert lines == ['I want', 'bubbles']

def test_splits_even_words_nicely():
    lines = splitter.split('download bubbles ordering form')

    assert lines == ['download', 'bubbles', 'ordering', 'form']


    
