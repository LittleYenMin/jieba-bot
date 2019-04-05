import pytest
import nlu

@pytest.fixture()
def source():
    return ['我', '喜歡', '看', '電視', '不', '喜歡', '看', '電影']


@pytest.fixture()
def target():
    return ['我', '不', '喜歡', '看', '電視', '也', '不', '喜歡', '看', '電影']


def test_cosine_similarity(source, target):
    assert nlu._consine_similarity(source, target) == 0.9381941874331419
