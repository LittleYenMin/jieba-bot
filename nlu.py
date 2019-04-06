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


def _consine_similarity(a: [str], b: [str]) -> float:
    words = set(a+b)
    vector_a = _word2vector(words, a)
    vector_b = _word2vector(words, b)
    return _cosine_theta(vector_a, vector_b)


def _cosine_theta(a: [int], b: [int]):
    numerator = sum(a * b for a, b in zip(a, b))
    denominator = _dot(a)*_dot(b)
    return numerator/denominator


def _dot(v: [int]) -> float:
    return sum(pow(n, 2) for n in v) ** 0.5


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
