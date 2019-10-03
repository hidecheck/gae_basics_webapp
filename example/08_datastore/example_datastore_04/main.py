import logging
from datetime import datetime

from flask import Flask

from google.cloud import datastore

app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    # res = insert()
    # res = get_all()
    key_id = 5672330625810432  # KeyIDを指定する
    # res = get_by_id(key_id)
    res = update(key_id)
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
    # データストアのクライアントオブジェクトを取得
    client = datastore.Client()

    # Queryオブジェクトを取得する
    query = client.query(kind='Example')

    # 日付の新しい順
    query.order = '-created'

    # クエリを実行する
    entities = list(query.fetch())

    # 全てのEntityにidプロパティを追加する
    for entity in entities:
        entity['id'] = entity.key.id

    # レスポンス用のJSONを作成する
    res = {
        'examples': entities
    }
    return res


def get_by_id(key_id):
    # データストアのクライアントオブジェクトを取得
    client = datastore.Client()

    # KeyIDを指定してKeyを生成する
    key = client.key('Example', key_id)

    # Keyを使ってEntityを取得する
    entity = client.get(key=key)

    # Entityが存在しなかった場合はエラーメッセージを返す
    if not entity:
        return {'message': 'Error: Resource not found.'}

    # entityにidプロパティを追加する
    entity['id'] = entity.key.id
    return entity


def update(key_id):
    # データストアのクライアントオブジェクトを取得
    client = datastore.Client()

    # Keyを使ってEntityを取得する
    key = client.key('Example', key_id)
    entity = client.get(key=key)

    # Entityが存在しなかった場合はエラーメッセージを返す
    if not entity:
        return {'message': 'Error: Resource not found.'}

    # Entityのプロパティを更新する
    entity['author'] = 'TSUYOSHI IGARASHI'

    # データストアに保存する
    client.put(entity)

    # entityにidプロパティを追加する
    entity['id'] = entity.key.id
    return entity


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
