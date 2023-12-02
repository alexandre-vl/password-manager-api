from src.utils.random import random, randomRange

import views
from flask import Flask, request, abort


app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)


if __name__ == '__main__':
    print(random())



    app.run(use_reloader=True)

    


