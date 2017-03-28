# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)

import moonfish.controller.views
import moonfish.models
