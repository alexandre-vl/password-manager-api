from src.utils.random_remaster import random, randomRange
from src.database.main import Database
from src.utils.chiffrage import encrypt, decrypt

print(random())
print(randomRange(1, 10))

database = Database()
print(database)
print(database.db_json())

