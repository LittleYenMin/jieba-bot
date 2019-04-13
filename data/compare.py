import nlu

from questions import ExampleQuestion


class Intent(object):
    def __init__(self, intent: str, score: float):
        self.intent = intent
        self.score = score

    def __repr__(self):
        return '<Intent {intent} {score}>'.format(
            intent=self.intent, score=self.score)


class QueryResult(object):

    def __set_top_scoring(self, intents: [Intent]):
        top_scoring_intent = None
        for intent in intents:
            if top_scoring_intent is not None:
                top_scoring_intent = intent if intent.score > top_scoring_intent.score else top_scoring_intent
            else:
                top_scoring_intent = intent
        self.topScoringIntent = top_scoring_intent

    def __init__(self, query_text: str, intents: [Intent]):
        self.query = query_text
        self.intents = intents
        self.__set_top_scoring(intents=intents)

    def __repr__(self):
        return '<QueryResult query {query} topScoringIntent {topScoringIntent} intents {intents}>'.format(
            query=self.query, topScoringIntent=self.topScoringIntent, intents=self.intents)


def questions(word: str, examples: [ExampleQuestion]) -> QueryResult:
    """
    >>> questions('question-1-3', [ExampleQuestion('question-1', 'answer-A'), ExampleQuestion('question-2', 'answer-B')])
    <QueryResult query question-1-3 topScoringIntent <Intent answer-A 0.8728715609439696> intents [<Intent answer-A 0.8728715609439696>, <Intent answer-B 0.6546536707079772>]>
            """
    intents = _questions(word, examples)
    result = [Intent(intent=intent, score=score)
              for intent, score in intents.items()]
    return QueryResult(query_text=word, intents=result)


def _questions(word: str, examples: [ExampleQuestion]) -> dict:
    """
    >>> _questions('question-1-3', [ExampleQuestion('question-1', 'answer-A'), ExampleQuestion('question-2', 'answer-B')])
    {'answer-A': 0.8728715609439696, 'answer-B': 0.6546536707079772}
        """
    intents = dict.fromkeys(list(q.command_type for q in examples), 0)
    for example in examples:
        command = example.command_type
        similarity = nlu.similarity(example.question, word)
        intents[command] = max(similarity, intents.get(command, 0))
    return intents
