# データベース設定やAPIリソースのルーティング設定
# Flask-RESTfulのadd_resource を利用することで、APIリソースの実装をapis に切り離す
from flask import Flask

from flask_restful import Api

from src.database import init_db
from src.apis.hoge import HogeListAPI, HogeAPI

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    init_db(app)

    api = Api(app)
    api.add_resource(HogeListAPI, '/hoges')
    api.add_resource(HogeAPI, '/hoges/<id>')

    return app

app = create_app()
