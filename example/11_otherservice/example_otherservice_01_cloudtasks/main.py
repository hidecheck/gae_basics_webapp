import logging

from flask import Flask, url_for, request
from google.cloud import tasks_v2


app = Flask(__name__)
logging.getLogger().setLevel(logging.DEBUG)


@app.route('/')
def home():
    # Taskクライアントを取得
    client = tasks_v2.CloudTasksClient()

    # プロジェクトID、ロケーション、キューID
    project = '<GCPプロジェクトID>'
    location = 'asia-northeast1'
    queue_id = 'my-queue'

    # タスクを処理するAppEngine タスクハンドラ
    relative_uri = url_for('run_task')

    # タスクの作成
    task = {
            'app_engine_http_request': {
                'http_method': 'POST',
                'relative_uri': relative_uri,
                'body': 'Hello Cloud Tasks!'.encode()
            }
    }

    # 完全修飾のキューの名前を作成
    parent = client.queue_path(project, location, queue_id)

    # タスクをキューに追加する
    task_response = client.create_task(parent, task)
    logging.info('Task {} がキューに追加されました'.format(task_response.name))
    res = {
        'message': 'Task {} がキューに追加されました'.format(task_response.name)
    }

    return res


@app.route('/run_task', methods=['POST'])
def run_task():
    logging.info('running!!!')
    payload = request.get_data(as_text=True)
    logging.info('payload={}'.format(payload))
    return '', 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
