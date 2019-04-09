import csv

from questions import ExampleQuestion


class Source:

    @staticmethod
    def from_csv(iterable: any) -> [ExampleQuestion]:
        questions = []
        content = csv.reader(iterable)
        next(content, None)  # escape headers is useless now
        for row in content:
            questions.append(
                ExampleQuestion(
                    question=row[0],
                    command_type=row[1]))
        return questions
