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

    comment = relationship('Comment', back_populates="article")


    def save_to_article(self, title, content, create_address, autor, status=1):
        with db.auto_commit():
            self.title = title
            self.content = content
            self.requester_name = create_address
            self.create_address = autor
            self.status = status
            db.session.add(self)
