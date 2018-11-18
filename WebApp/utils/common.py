#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/11/17


import hashlib

def md5(original):
    m2 = hashlib.md5()
    m2.update(original.encode('utf8'))
    return m2.hexdigest()
