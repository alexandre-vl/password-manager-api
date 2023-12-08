from src.utils.random_remaster import random, randomRange
from src.database.main import Database

import views
from flask import Flask, request, abort

database = Database("db.json")

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)

@app.route('/api', methods=['GET'])
def api():
    return "Api is working"

@app.route('/api/item', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_item():
    db_json = database.read_json()

    # GET PASSWORD FUNCTION
    if request.method == 'GET':
        id_param = request.args.get('id')
        if not id_param:
            return "No ID param found", 400
        try:
            if not int(id_param):
                return "Incorrect ID", 400

            found_item = next((x for x in db_json if x['id'] == int(id_param)), None)
            
            if not found_item:
                return "No item found", 404
            return found_item
        except ValueError:
            return "Incorrect ID", 400

    # CREATE ITEM FUNCTION
    elif request.method == 'POST':
        credential = request.args.get('credential')
        value = request.args.get('value')
        website = request.args.get('website')

        if not credential or not value or not website:
            return "Please provide all necessary params", 400
        

        last_id = (0 if len(db_json) == 0 else int(db_json[-1]['id'])) + 1
        if not last_id:
            return "Internal servor error", 500
        
        found_item = next((x for x in db_json if x['website'] == website), None)
        if found_item:
            return "You already have a password for this website", 400


        database.append({
            "id": last_id,
            "credential": credential,
            "value": value,
            "website": website,
            "isFavorite": False
        })
        


        return "Post"
    elif request.method == 'PUT':
        return "Put"
    elif request.method == 'DELETE':
        return "Delete"
    else:
        abort(404)



if __name__ == '__main__':
    app.run(use_reloader=True)

    


