#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17
from sqlalchemy.orm import relationship

from WebApp.models.base import Base
from sqlalchemy import Column, Integer, String, Text

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True, doc='自增长ID')
    title = Column(String(50), nullable=False, default='a', doc='文章标题')
    content = Column(Text, nullable=False, default='b', doc='文章内容')
    create_address = Column(String(32), nullable=False, default='d', doc='创作地址')

    comment = relationship('Comment', back_populates="article")
