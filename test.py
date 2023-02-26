from random import randrange
import json

facts = json.load(open("./facts.json", "r"))

print(facts[randrange(len(facts))])
