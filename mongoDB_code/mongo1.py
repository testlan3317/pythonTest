# create "mydatabase" database

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]  # create database, but not show until the first data in there. 
