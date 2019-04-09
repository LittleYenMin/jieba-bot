from csv import reader as csv_reader

from questions import ExampleQuestion


class Source:

    @staticmethod
    def from_csv(path: str) -> [ExampleQuestion]:
        questions = []
        with open(path, 'r', encoding='utf-8') as f:
            csv = csv_reader(f)
            next(csv, None)  # escape headers is useless now
            for row in csv:
                questions.append(
                    ExampleQuestion(
                        question=row[0],
                        command_type=row[1]))
        return questions
