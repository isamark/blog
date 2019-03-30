#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17


from sqlalchemy import Column, String, Integer, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Comment(Base):

    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True, doc='自增长ID')
    # uid = Column(Integer, ForeignKey('user.id'), doc='用户id')
    content = Column(String(1024), nullable=False, default='', doc='评论内容')

    # user = relationship('User', back_populates="comment")

    a_id = Column(Integer, ForeignKey('article.id'), doc='文章ID')
    article = relationship('Article', back_populates="comment")
