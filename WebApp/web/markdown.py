#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2019/8/25
import datetime


from . import web
from WebApp.forms import ArticleForm
from flask import render_template, redirect, url_for
from WebApp.models.article import Article


@web.route('/test1', methods=['GET', 'POST'])
def test_1():
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

    if form.validate_on_submit():
        # 文章内容以markdown的格式存储，需要显示页面时可通过markdown模块解析后显示。如
        # print(markdown.markdown(form.content.data))
        article = Article()
        article.save_to_article(title=form.title.data, content=form.content.data, create_address=form.create_address.data, autor=form.autor.data)

        return redirect(url_for('web.get_article_list'))
    return render_template('post_edit.html', form=form)
