import cmath
import jieba

command_map = {'曠課': '昌昌;曠課', '課表': '昌昌;課表', '成績': '昌昌;成績'}


def response_message(text: str) -> list:
    messages = []
    cmds = _get_commands(jieba.cut(text))
    for cmd in cmds:
        messages.append(_exec_command(cmd))
    return messages


def _get_commands(text_sequence: [str]) -> set:
    possible_commands = set()
    for text in text_sequence:
        cmd = command_map.get(text)
        if cmd is not None:
            possible_commands.add(cmd)
    return possible_commands


def _similarity(a: [str], b: [str]) -> float:
    words = set(a+b)
    vector_a = _get_vec(words, a)
    vector_b = _get_vec(words, b)
    return _consine_similarity(vector_a, vector_b)


def _consine_similarity(a: [int], b: [int]):
    if len(a) != len(b):
        raise ValueError('list a and list b must have the same length')
    numerator = sum(expression1 * expression2 for expression1, expression2 in zip(a, b))
    denominator = _dot(a)*_dot(b)
    return numerator/denominator


def _dot(vec: [int]) -> float:
    return cmath.sqrt(
        sum(pow(v, 2) for v in vec)
    )


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
