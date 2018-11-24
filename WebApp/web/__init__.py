#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2018/10/28

from flask import Blueprint


web = Blueprint('web', __package__)

from WebApp.web import article
