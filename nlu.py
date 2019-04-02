import jieba

def response_message(text: str) -> str:
    split_text = jieba.cut(text)
    return ", ".join(split_text)
