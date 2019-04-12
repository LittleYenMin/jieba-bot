import csv

import questions


def from_csv_file(path: str) -> [questions.ExampleQuestion]:
    with open(path, 'r', encoding='utf-8') as f:
        return from_csv(f)


def from_csv(iterable: any) -> [questions.ExampleQuestion]:
    result = []
    csv_reader = csv.reader(iterable)
    next(csv_reader, None)  # escape headers is useless here.
    for row in csv_reader:
        result.append(
            questions.ExampleQuestion(
                question=row[0],
                command_type=row[1]))
    return result
