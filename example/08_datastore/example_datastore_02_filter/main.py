import logging
from datetime import datetime

from flask import Flask

from google.cloud import datastore

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    # res = insert()
    res = get_all()

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


def get_all():
    client = datastore.Client()
    # Queryオブジェクトを取得する
    query = client.query(kind='Example')

    # Filterを追加
    query.add_filter('author', '=', 'Mai Shirakawa')

    # 日付の新しい順 コメントアウト
    # query.order = '-created'

    # クエリを実行する
    entities = list(query.fetch())

    # 全てのentityにidプロパティを追加する
    for entity in entities:
        entity['id'] = entity.key.id

    # レスポンス用のJSONを作成する
    res = {
        'examples': entities
    }
    return res


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
