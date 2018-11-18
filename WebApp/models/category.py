#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17


from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.orm import relationship

from .base import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True, doc='自增长ID')
    name = Column(String(64), nullable=True, default='', doc='分类名称')

    article = relationship('Article', back_populates="category")
