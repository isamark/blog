#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Amark"
# Date: 2018/7/18


from WebApp import create_app


app = create_app()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=app.config.get('DEBUG'))