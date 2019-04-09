import pytest
import io
import data.source


def test_get_from_csv():
    f = io.StringIO("""﻿question,answer
我要查曠課,昌昌;曠課
我要查課表,昌昌;課表
我要查成績,昌昌;成績
""")
    questions = data.source.from_csv(f)
    assert len(questions) == 3
