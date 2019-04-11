import logging
import pytest
import jieba
import nlu


jieba.setLogLevel(logging.ERROR)
jieba.initialize()


def test_cosine_similarity():
    question = '我要查成績'
    user_input = '查成績'
    other_input = '我成績沒考好'
    user_input_similarity = nlu.similarity(question, user_input)
    other_input_similarity = nlu.similarity(question, other_input)
    # user input is more similar then other_input
    assert user_input_similarity > other_input_similarity
