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


def _exec_command(cmd: str) -> str:
    """exec the command and return response

    Parameters:
        cmd (str): The string represented command

    Returns:
        response (str): The string for text response
    """
    pass
