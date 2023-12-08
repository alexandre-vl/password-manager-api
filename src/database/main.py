import json

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.path = "src/database/" + self.db_name

    def create(self):
        try:
            with open(self.path, "x") as db:
                db.write("[]")
        except FileExistsError:
            pass

    def read(self):
        with open(self.path, "r") as db:
            return json.load(db)

    def read_json(self):
        with open(self.path, "r") as db:
            return json.loads(db.read())
        
    def write(self, data):
        with open(self.path, "w") as db:
            json.dump(data, db, indent=4)
    
    def append(self, data):
        with open(self.path, "r") as db:
            db_data = json.load(db)
            db_data.append(data)
            print(db_data)
            with open(self.path, "w") as db:
                json.dump(db_data, db, indent=4)

