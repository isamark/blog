#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/10/28


# from tornado.web import authenticated
from sqlalchemy import desc

from . import web
from WebApp.models.user import User
from WebApp.models.article import Article
from WebApp.models.comment import Comment
from flask import render_template, request
# from ext import db
# from ext import db

@web.route('/')
def get_article_list():

    p = Article.query.filter().order_by(desc(Article.id)).first()

    return render_template('index.html', post=p)