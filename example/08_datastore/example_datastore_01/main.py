import logging
from datetime import datetime

from flask import Flask

from google.cloud import datastore

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    res = insert()

    return res


def insert():
    # データストアのクライアントオブジェクトを取得
    client = datastore.Client()

    # Exampleカインドに保存するためののKeyを作成
    key = client.key('Example')

    # Entityを作成し、プロパティを設定する
    entity = datastore.Entity(key=key)
    entity['author'] = 'Tsuyoshi Igarashi'
    entity['created'] = datetime.now()

    # データストアに保存する
    client.put(entity)

    # entityにidプロパティを追加する
    entity['id'] = entity.key.id

    # entityを返す
    return entity


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
