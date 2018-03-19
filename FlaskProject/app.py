# -*- coding: utf-8 -*-

from flask           import Flask
from flask_flatpages import FlatPages   #  are these being used at all ?
from flask_frozen    import Freezer

app     = Flask(__name__)
app.config.from_pyfile('settings.py')

pages   = FlatPages(app)
freezer = Freezer(  app)
