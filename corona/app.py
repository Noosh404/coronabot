from flask import Flask

app = Flask(__name__)

from .views import *


def main():
    app.run(host="0.0.0.0", debug=True)
