#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/11/17


import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger, String, Text


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db=SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.datetime.now().timestamp())


