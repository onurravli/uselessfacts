from flask import Flask
from random import randrange
import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'facts.json')

facts = json.load(open(data_file, "r"))

app = Flask(__name__)


@app.route('/')
def home():
    return facts[randrange(len(facts))]
