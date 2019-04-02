import jieba

def execute(text: str) -> str:
    split_text = jieba.cut(text)
    return ", ".join(jieba.cut(text))
