import jieba


def response_message(text: str) -> str:
    cmd = _get_command(jieba.cut(text))
    return _exec_command(cmd)


def _get_command(text_sequence: [str]) -> str:
    for text in text_sequence:
        if text == '曠課':
            return '昌昌;曠課'


def _exec_command(cmd: str) -> str:
    """exec the command and return response

    Parameters:
        cmd (str): The string represented command

    Returns:
        response (str): The string for text response
    """
    pass
