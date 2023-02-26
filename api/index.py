from flask import Flask
from random import randrange
import json

app = Flask(__name__)
facts = json.load(open("facts.json", "r"))


@app.route('/')
def home():
    return facts[randrange(len(facts))]
