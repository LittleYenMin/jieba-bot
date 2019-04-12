import nlu

from questions import ExampleQuestion


def questions(word: str, questions: [ExampleQuestion]) -> dict:
    """
        >>> questions('我想查成績', [ExampleQuestion('我想查成績', '成績'), ExampleQuestion('我想查曠課', '曠課')])
        {'成績': 0.9999999999999998, '曠課': 0.4999999999999999}
        """
    intents = dict.fromkeys(list(q.command_type for q in questions), 0)
    for question in questions:
        command = question.command_type
        similarity = nlu.similarity(question.question, word)
        intents[command] = max(similarity, intents.get(command, 0))
    return intents
