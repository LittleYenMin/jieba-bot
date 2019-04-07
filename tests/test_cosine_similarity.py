import logging
import pytest
import jieba
import nlu


jieba.setLogLevel(logging.ERROR)
jieba.initialize()


def similarity(question, segment) -> float:
    question_list = jieba.lcut(question)
    segment_list = jieba.lcut(segment)
    return nlu._similarity(question_list, segment_list)


def test_cosine_similarity():
    question_segment = ['我', '要', '查', '成績']
    user_input_segment = ['我', '想', '查', '成績']
    other_input_segment = ['我', '成績', '沒', '考', '好']
    user_input_similarity = nlu._similarity(question_segment, user_input_segment)
    other_input_similarity = nlu._similarity(question_segment, other_input_segment)
    # user input is more similar then other_input
    assert user_input_similarity > other_input_similarity
