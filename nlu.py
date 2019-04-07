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
    vector_a = _word2vector(words, a)
    vector_b = _word2vector(words, b)
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


def _word2vector(all_words: set, text_sequence: [str]) -> [int]:
    frequency = dict.fromkeys(all_words, 0)
    for text in text_sequence:
        if text in all_words:
            value = frequency.get(text)
            if value is None:
                value = 1
            else:
                value += 1
            frequency[text] = value
        else:
            frequency[text] = 0
    return list(frequency.values())


def _exec_command(cmd: str) -> str:
    """exec the command and return response

    Parameters:
        cmd (str): The string represented command

    Returns:
        response (str): The string for text response
    """
    pass
