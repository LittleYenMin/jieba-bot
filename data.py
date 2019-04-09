import csv
from questions import Questions


class Source:

    @staticmethod
    def from_csv(path: str = './data.csv') -> [Questions]:
        questions = []
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # headers
            _ = next(reader, None)
            for row in reader:
                questions.append(Questions(question=row[0], answer=row[1]))
        return questions
