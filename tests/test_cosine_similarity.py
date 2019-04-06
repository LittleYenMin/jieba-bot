import pytest
import nlu


def test_cosine_similarity():
    question_segment = ['我', '要', '查', '成績']
    user_input_segment = ['我', '想', '查', '成績']
    other_input_segment = ['我', '成績', '沒', '考', '好']
    user_input_similarity = nlu._consine_similarity(question_segment, user_input_segment)
    other_input_similarity = nlu._consine_similarity(question_segment, other_input_segment)
    # user input is more similar then other_input
    print(user_input_similarity, other_input_similarity)
    assert user_input_similarity > other_input_similarity
