from src.utils.random_remaster import random, randomRange
from src.database.main import Database

import views
from flask import Flask, request, abort

database = Database("db.json")

print(database.read())

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)

@app.route('/api', methods=['GET'])
def api():
    return "Api is working"

@app.route('/api/item', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_item():
    db_json = database.read_json()

    if request.method == 'GET':
        id_param = request.args.get('id')
        if not id_param:
            abort(404)
        found_item = next((x for x in db_json if x['id'] == int(id_param)), None)

        return found_item

    elif request.method == 'POST':
        return "Post"
    elif request.method == 'PUT':
        return "Put"
    elif request.method == 'DELETE':
        return "Delete"
    else:
        abort(404)



if __name__ == '__main__':
    """ for i in range(1000):
        print(randomRange(1, 10)) """

    app.run(use_reloader=True)

    


