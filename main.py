from flask import Flask
import random

app = Flask(__name__)

# print(random.__name__)
# print(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"\
"<p>This is me baddie and unstoppable</p>"\
"<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzN2N2QycW9rcDdseWhoaHF2djd2MTR5MWhkbzRucWNrM2Fqd3lvaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pgb4zlVQqnUB2/giphy.gif' width=200px>"

# decorator function

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined

def say_bye():
    return "Bye!!"


# Creating variable path and converting the path to a specified data type
@app.route("/username/<path:name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}, you are {number} years old"


# does the same as flask run
if __name__=="__main__":
    app.run(debug=True)