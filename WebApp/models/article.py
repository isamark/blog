#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17
from sqlalchemy.orm import relationship

from WebApp.models.base import Base
from sqlalchemy import Column, Integer, String, Text

from WebApp.models.base import db


class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True, doc='自增长ID')
    title = Column(String(50), nullable=False, default='a', doc='文章标题')
    content = Column(Text, nullable=False, default='b', doc='文章内容')
    create_address = Column(String(32), nullable=False, default='d', doc='创作地址')
    autor = Column(String(32), nullable=False, default='', doc='作者')
    profile = Column(String(1028), nullable=False, default='', doc='文章简介')
    pic = Column(String(128), nullable=False, default='', doc='文章配图')

    comment = relationship('Comment', back_populates="article")


    def save_to_article(self, title, content, create_address, autor, profile, pic, status=1):
        with db.auto_commit():
            self.title = title
            self.content = content
            self.create_address = create_address
            self.autor = autor
            self.autor = autor
            self.profile = profile
            self.pic = pic
            db.session.add(self)

    def update_article(self, id, title, content, create_address, autor, profile, pic):
        Article.query.filter(Article.id == id).update({'title': title, 'content': content, 'create_address': create_address, 'autor': autor, 'profile': profile, 'pic': pic})
        db.session.commit()
