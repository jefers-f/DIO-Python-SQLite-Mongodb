import datetime
import pprint

import pymongo

client = pymongo.MongoClient("mongodb+srv://jfarcdt:grr20102632@cluster1.ejfes0s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")


db = client.test
collections = db.test_collection
print(db.test_collection)

post = {
    'author':'Mike',
    'text':'My first mongodb app on python',
    'tags':['mongodb','python'],
    'date': datetime.datetime.now()
}

new_post  = [{
    'author':'Jhon',
    'text':'My mongodb app on python again',
    'tags':['mongodb','python', 'pymongo'],
    'date': datetime.datetime.now()
    },
    {
    'author':'Pedro',
    'text':'My mongodb app on python again 2',
    'title':'Mongo is fun',
    'tags':['mongodb','python', 'pymongo'],
    'date': datetime.datetime.now()
    }]

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

result = posts.insert_many(new_post)
print(result.inserted_ids)

pprint.pprint(db.posts.find_one({'author':'Jhon'}))

