# /usr/bin/python3
import views
from flask import Flask, request, abort

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)


if __name__ == '__main__':
    app.run(use_reloader=True)

