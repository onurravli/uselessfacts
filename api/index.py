from flask import Flask
from random import randrange
import json

facts = json.load(open("facts.json", "r"))

app = Flask(__name__)


@app.route('/')
def home():
    return facts[randrange(len(facts))]


@app.route('/about')
def about():
    return 'About'
