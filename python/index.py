import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['pymongo']
userCol = db['user']
user = {"name": "hieu", "age": 20}
# print(userCol.insert_one(user).inserted_id)
userFound = userCol.find({"age": {"$gt": 20}})
for user in userFound:
  print(user['name'])
