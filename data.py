from csv import reader as csv_reader

from questions import Questions


class Source:

    @staticmethod
    def from_csv(path: str) -> [Questions]:
        questions = []
        with open(path, 'r', encoding='utf-8') as f:
            csv = csv_reader(f)
            next(csv, None)  # escape headers is useless now
            for row in csv:
                questions.append(Questions(question=row[0], answer=row[1]))
        return questions
