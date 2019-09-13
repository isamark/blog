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
from flask import render_template, request, redirect, url_for


# from ext import db
# from ext import db

@web.route('/')
def get_article_list():

    p = Article.query.filter().order_by(desc(Article.id)).all()
    p = [{'id': e.id, 'title': e.title, 'autor': e.autor, 'content': e.content[:20], 'create_address': e.create_address, 'profile': e.profile, 'pic': e.pic} for e in p]
    return render_template('index.html', posts=p)

@web.route('/detail')
def detail():
    if not request.args.get('id'):
        return redirect(url_for('web.get_article_list'))

    p = Article.query.filter(Article.id == request.args.get('id')).order_by(desc(Article.id)).first()
    p = {'title': p.title, 'autor': p.autor, 'content': p.content, 'create_address': p.create_address, 'profile': p.profile, 'pic': p.pic}
    return render_template('single.html', post=p)