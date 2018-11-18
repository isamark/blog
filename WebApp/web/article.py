#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/10/28


from . import web
from WebApp.models.user import User
from WebApp.models.article import Article
from WebApp.models.comment import Comment
from WebApp.models.category import Category
from flask import render_template


@web.route('/article_list')
def get_article_list():


    return render_template('index.html')