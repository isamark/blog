#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2019/8/25
import datetime

import logging

from sqlalchemy import desc

from . import web
from WebApp.forms import ArticleForm
from flask import render_template, redirect, url_for, request
from WebApp.models.article import Article



@web.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    mkd = '''
    # header
    ## header2
    [picture](http://www.example.com)
    * 1
    * 2
    * 3
    **bold**
    '''
    form = ArticleForm()
    a = {}
    if id and not request.args.get('origin'):
        p = Article.query.filter(Article.id == id).order_by(desc(Article.id)).first()

        form.title.data = p.title
        form.autor.data = p.autor
        form.create_address.data = p.create_address
        form.content.data = p.content
        form.profile.data = p.profile
        form.pic.data = p.pic
        a.update({"id": p.id})

    else:
        a.update({"id": 0})

    if form.validate_on_submit():
        # 文章内容以markdown的格式存储，需要显示页面时可通过markdown模块解析后显示。如
        # print(markdown.markdown(form.content.data))
        article = Article()
        if not id:
            print("$$$" * 100)
            logging.info(form.title.data)
            logging.info("test_1执行")
            article.save_to_article(title=form.title.data, content=form.content.data, create_address=form.create_address.data, autor=form.autor.data, profile=form.profile.data, pic=form.pic.data)
        else:
            article.update_article(id=id, title=form.title.data, content=form.content.data, create_address=form.create_address.data, autor=form.autor.data, profile=form.profile.data, pic=form.pic.data)

        return redirect(url_for('web.get_article_list'))
    return render_template('post_edit.html', form=form, post=a)
