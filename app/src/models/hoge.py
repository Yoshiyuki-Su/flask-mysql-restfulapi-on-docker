# APIリソースで利用、Flask-Migrateでマイグレーションする際に利用
from datetime import datetime

from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields

from src.database import db

ma = Marshmallow()


class HogeModel(db.Model):
    __tablename__ = 'hoges'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(255), nullable=False)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __repr__(self):
        return '<HogeModel {}:{}>'.format(self.id, self.name)


class HogeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HogeModel

    createTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updateTime = fields.DateTime('%Y-%m-%dT%H:%M:%S')
