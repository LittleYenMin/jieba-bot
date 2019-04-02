import pytest
import nlu

@pytest.fixture()
def text():
    return '我想查曠課'

def test_nlu_execute(text):
    assert nlu.execute(text) == '我想查, 曠課'
