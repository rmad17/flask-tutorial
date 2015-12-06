#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 rmad <rmad@rmad-mint>
#
# Distributed under terms of the MIT license.

"""

"""
from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/templates')
def test_template():
    user = {'nickname': 'rmad17'}  # fake user
    return render_template('hello.html', title='Home', user=user)
