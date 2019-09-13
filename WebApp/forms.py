#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019/8/25


from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Required

class ArticleForm(FlaskForm):


	title = StringField(u"标题", validators=[DataRequired()])
	autor = StringField(u'作者',validators=[DataRequired()])
	create_address = StringField(u"创作地址", validators=[DataRequired()])
	content = TextAreaField(u"正文", validators=[DataRequired()])
	profile = StringField(u"文章简介", validators=[DataRequired()])
	pic = StringField(u"文章配图", validators=[DataRequired()])
	submit = SubmitField(u"发布")

	def __init__(self):
		super(ArticleForm,self).__init__()

