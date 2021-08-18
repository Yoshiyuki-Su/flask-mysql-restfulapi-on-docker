# データベースを利用するための初期化処理やマイグレーション管理のために必要なメソッドを定義
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    Migrate(app, db)
