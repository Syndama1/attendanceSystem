"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
from website.pythonScripts import clubDataModule

import website.views

dataPath = 'website/data'

