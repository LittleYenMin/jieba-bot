import math
import jieba

command_map = {'曠課': '昌昌;曠課', '課表': '昌昌;課表', '成績': '昌昌;成績'}


def similarity(a: str, b: str) -> float:
    return _similarity(jieba.lcut(a), jieba.lcut(b))


def _similarity(a: [str], b: [str]) -> float:
    words = set(a + b)
    vector_a = _get_vec(words, a)
    vector_b = _get_vec(words, b)
    return _consine_similarity(vector_a, vector_b)


def _consine_similarity(a: [int], b: [int]) -> float:
    if len(a) != len(b):
        raise ValueError('vector a len: {} and vector b len: {} must have the same length'.format(len(a), len(b)))
    numerator = sum(x1 * x2 for x1, x2 in zip(a, b))
    denominator = _dot(a) * _dot(b)
    return numerator / denominator


def _dot(vec: [int]) -> float:
    temp = sum(pow(v, 2) for v in vec)
    return math.sqrt(temp)


def _get_vec(all_words: set, seq: [str]) -> [int]:
    vec = [0] * len(all_words)
    for i, word in enumerate(all_words):
        for v in seq:
            if v == word:
                vec[i] += 1
    return vec


def _exec_command(cmd: str) -> str:
    """exec the command and return response

    Parameters:
        cmd (str): The string represented command

    Returns:
        response (str): The string for text response
    """
    pass
