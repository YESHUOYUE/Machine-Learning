# ！/user/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, current_app, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:happylifeCYX@127.0.0.1:3306/happylife'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'xxxxxxx'

db = SQLAlchemy(app)  # 实例化数据库

class todolist(db.Model):
    __tablename__ = "todolist"
    id = db.Column(db.INT, primary_key=True)
    title = db.Column(db.VARCHAR(50))
    content = db.Column(db.VARCHAR(200))
    status = db.Column(db.VARCHAR(10), nullable=False)
    add_time = db.Column(db.INT, nullable=False)
    deadline = db.Column(db.INT)

if __name__ == "__main__":
    with app.app_context():
        print(current_app.name)
        db.create_all()
