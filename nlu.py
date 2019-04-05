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


def _consine_similarity(question: [str], text_sequence: [str]) -> float:
    words = set(question+text_sequence)
    question_frequency = _get_frequency(words, question)
    text_frequency = _get_frequency(words, text_sequence)
    return _cosine_theta(question_frequency, text_frequency)


def _cosine_theta(a: [int], b: [int]):
    denominator = (sum(pow(n, 2) for n in a) ** 0.5)*(sum(pow(n, 2) for n in b) ** 0.5)
    numerator = sum(a[i] * b[i] for i in range(len(a)))
    return numerator/denominator


def _get_frequency(source: set, text_sequence: [str]) -> [int]:
    frequency = {}
    for text in text_sequence:
        if text in source:
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
