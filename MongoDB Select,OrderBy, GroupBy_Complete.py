#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')



db = client['books']



books = db.books



db.books.insert_many([{"book": "The Ranch", "author": "Danielle Steel"},
                                {"book": "The Firm", "author": "John Grisham"},
                                {"book": "The runaway jury", "author": "John Grisham"},
                                {"book": "Time to kill", "author": "John Grisham"},
                                {"book": "The testament", "author": "John Grisham"},
                                {"book": "Tell me your Dreams", "author": "Sidney Sheldon"}
                              ])



for book in books.find():
  print(book)



books.find_one({'author':"Danielle Steel"})



for book in books.find({'author':"Sidney Sheldon"}):
    print(book)



for book in books.find({'author':"John Grisham"}):
    print(book['book'])



for book in books.find().sort([("author", pymongo.ASCENDING)]):
  print(book)



pipeline = [
     {"$group": {"_id": "$author", "count": {"$sum": 1}}}]

grp_books = db.books.aggregate(pipeline)



for book in grp_books:
  print(book)

