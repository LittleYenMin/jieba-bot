import pytest
import nlu


def test_cosine_similarity():
    question = ['a', 'b']
    user_input = ['a', 'c']
    other_input = ['c']
    user_input_similarity = nlu._consine_similarity(question, user_input)
    other_input_similarity = nlu._consine_similarity(question, other_input)
    # user input is more similar then other_input
    assert user_input_similarity > other_input_similarity
