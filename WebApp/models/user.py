#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17


from sqlalchemy import Integer, SmallInteger, String, Column
from sqlalchemy.orm import relationship

from .base import Base
from WebApp.utils.common import md5


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True, doc='自增长ID')
    username = Column(String(32), nullable=False, default='', doc='用户名')
    _password = Column('password', String(256), doc='登陆密码')
    email = Column(String(50), unique=True, nullable=False, doc='电子邮件')
    wx_open_id = Column(String(50), nullable=False, default='', doc='用户open_id')
    wx_nickname = Column(String(32), nullable=False, default='', doc='用户昵称')


    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, raw):
        self._password = md5(raw)

