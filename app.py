import os
import json

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import data.source
import data.compare

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    result = data.compare.questions(word=event.message.text, samples=data.source.from_csv_file('./data.csv'))
    json_str = json.dumps(result, default=lambda o: o.__dict__, ensure_ascii=False)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=json_str))


if __name__ == "__main__":
    app.run()
