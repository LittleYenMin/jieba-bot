class Questions:

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return '<Questions {question} {answer}>'.format(
            question=self.question, answer=self.answer)
