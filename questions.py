class ExampleQuestion:

    def __init__(self, question: str, command_type: str):
        self.question = question
        self.command_type = command_type

    def __repr__(self):
        return '<Questions {question} {command_type}>'.format(
            question=self.question, command_type=self.command_type)
