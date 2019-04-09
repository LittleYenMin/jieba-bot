import csv

from questions import ExampleQuestion


class Source:

    @staticmethod
    def from_csv(iterable: any) -> [ExampleQuestion]:
        questions = []
        csv_reader = csv.reader(iterable)
        next(csv_reader, None)  # escape headers is useless now
        for row in csv_reader:
            questions.append(
                ExampleQuestion(
                    question=row[0],
                    command_type=row[1]))
        return questions
