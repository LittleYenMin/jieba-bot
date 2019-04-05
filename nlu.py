import jieba

command_mapping = {'曠課': '昌昌;曠課', '課表': '昌昌;課表', '成績': '昌昌;成績'}


def response_message(text: str) -> str:
    cmds = _get_commands(jieba.cut(text))
    return _exec_command(cmds)


def _get_commands(text_sequence: [str]) -> set:
    commands = set()
    for text in text_sequence:
        if text in command_mapping:
            commands.add(command_mapping.get(text))
    return commands


def _exec_command(cmds: set) -> str:
    """exec the command and return response

    Parameters:
        cmd (str): The string represented command

    Returns:
        response (str): The string for text response
    """
    pass
