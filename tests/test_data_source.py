import pytest
import io
import data.source


def test_get_from_csv():
    f = io.StringIO("""﻿question,answer
question1,answer1
question2,answer2
question3,answer3
""")
    questions = data.source.from_csv(f)
    assert len(questions) == 3
