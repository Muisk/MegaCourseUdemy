import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate (w):
    w = w.lower()
    if w in data:
        return data [w]
    elif data.keys()==:
        return 
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word:")
print(translate(word))