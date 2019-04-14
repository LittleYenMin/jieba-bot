import csv
import json
import operator

import nlu
import questions


class Similarity(object):
    def __init__(self, intent: str, score: float):
        self.intent = intent
        self.score = score

    def __repr__(self):
        return '<Intent {intent} {score}>'.format(
            intent=self.intent, score=self.score)


class SimilarityResult(object):

    def __init__(self, query_text: str, intents: [Similarity]):
        self.query = query_text
        self.intents = intents

    def __repr__(self):
        return '<QueryResult query {query} topScoringIntent {topScoringIntent} intents {intents}>'.format(
            query=self.query, topScoringIntent=self.topScoringIntent, intents=self.intents)

    @property
    def intents(self):
        return self._intents

    @intents.setter
    def intents(self, intents: [Similarity]):
        self._intents = intents
        self.topScoringIntent = max(self.intents, key=operator.attrgetter('score'))

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)


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


def compare_questions(word: str, samples: [questions.ExampleQuestion]) -> SimilarityResult:
    intents = _questions(word, samples)
    return SimilarityResult(query_text=word, intents=intents)


def _questions(word: str, samples: [questions.ExampleQuestion]) -> [Similarity]:
    """
    >>> _questions('question-1-3', [questions.ExampleQuestion('question-1', 'answer-A'), questions.ExampleQuestion('question-2', 'answer-B')])
    [<Intent answer-A 0.8728715609439696>, <Intent answer-B 0.6546536707079772>]
    """
    intents = dict.fromkeys(list(q.command_type for q in samples), 0)
    for sample in samples:
        command = sample.command_type
        similarity = nlu.similarity(sample.question, word)
        intents[command] = max(similarity, intents.get(command, 0))
    return [Similarity(intent=intent, score=score)
            for intent, score in intents.items()]
