#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/10/28

from flask import Flask
from WebApp.models.base import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('configs')
    app.config.from_pyfile('./config.cfg', silent=True)
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from web import web
    app.register_blueprint(web)
