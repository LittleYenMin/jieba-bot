import operator
import nlu

from questions import ExampleQuestion


class Intent(object):
    def __init__(self, intent: str, score: float):
        self.intent = intent
        self.score = score

    def __repr__(self):
        return '<Intent {intent} {score}>'.format(
            intent=self.intent, score=self.score)


class SimilarityResult(object):

    def __init__(self, query_text: str, intents: [Intent]):
        self.query = query_text
        self.intents = intents

    def __repr__(self):
        return '<QueryResult query {query} topScoringIntent {topScoringIntent} intents {intents}>'.format(
            query=self.query, topScoringIntent=self.topScoringIntent, intents=self.intents)

    @property
    def intents(self):
        return self._intents

    @intents.setter
    def intents(self, intents: [Intent]):
        self._intents = intents
        self.topScoringIntent = max(self.intents, key=operator.attrgetter('score'))


def questions(word: str, samples: [ExampleQuestion]) -> SimilarityResult:
    intents = _questions(word, samples)
    return SimilarityResult(query_text=word, intents=intents)


def _questions(word: str, samples: [ExampleQuestion]) -> [Intent]:
    """
    >>> _questions('question-1-3', [ExampleQuestion('question-1', 'answer-A'), ExampleQuestion('question-2', 'answer-B')])
    [<Intent answer-A 0.8728715609439696>, <Intent answer-B 0.6546536707079772>]
    """
    intents = dict.fromkeys(list(q.command_type for q in samples), 0)
    for sample in samples:
        command = sample.command_type
        similarity = nlu.similarity(sample.question, word)
        intents[command] = max(similarity, intents.get(command, 0))
    return [Intent(intent=intent, score=score)
            for intent, score in intents.items()]
