import pymongo
from pymongo import MongoClient
# from pymongo import ObjectId


import pprint as pp
from util import getDate

ip = 'localhost'
port=27017

class mongoDB():
    def __init__(self,date):
        self.date=date
        self.conn = MongoClient(ip,port) # get connection with DB
        self.db = self.conn.temp # getting 
        self.table = self.db.temp # 실질적인 table.
        # print(self.db.list_collection_names())

    def makeModel(self,video_code,bow):
        result = {
            "_id":video_code,
            "data" : bow,
            "date" : self.date
            }
        
        return result

    def insert(self,video_code,bow):
        self.table.insert_one(self.makeModel(video_code,bow))

    def find_id(self,id):
        item = self.table.find_one({'_id':str(id)})
        return item["data"]
    
    def find_all(self): # top 10 
        items = self.table.find()
        result = []
        for item in items:
            srt_bow = sorted(item["bow"],key=lambda x : -x[1] )
            result.append(srt_bow[:10])
        return result

# mongoDB(getDate())
# print(mongoDB(getDate()).conn.list_database_names()) # db 확인
# temp = mongoDB(getDate())
# temp.insert("temp112452222",{"tt32":12331422})
# print(temp.find_id("temp"))
# # print(temp.find_all())

# print("!@34356768")

# =================================
# conn = MongoClient(ip,port)

# print(conn.list_database_names()) # db 확인
# db = conn.test_db
# posts = db.posts
# print(posts.find_one())
# print(db.list_collection_names())

# def makeModel(bow):
#     result = {
#         "_id": 210424,
#         "bow": bow
#     }
#     return result

# data = [("big",33),("fuck",34),("dannm",21),("clown",311),("lost",52)]
# posts.insert_one(makeModel(data))
# post_id = posts.insert_one(post).inserted_id

# print(post_id)
# pp.pprint(posts.find_one({"_id":"210426"}))
# for i in posts.find():
#     pp.pprint(i)
        



    
