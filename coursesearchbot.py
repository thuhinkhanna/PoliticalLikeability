import praw
import sys
from praw.models import MoreComments
import pandas as pd
from pymongo import MongoClient
# OAuth
reddit = praw.Reddit( 
        client_id="Z8chjFnnwYysVXaVGU1SNw", 
        client_secret="7UHH7gdjAtV8dZXIN16-Eo-_8x4lrQ", 
        password="crazybasuke", 
        user_agent="coursesearchbot by u/coursebotadmin", 
        username="coursebotadmin" )

document = {}
results = reddit.subreddit("all").search('Stanford Machine Learning Coursera review')
document["title"] = "Stanford Machine Learning Coursera"
# Result has a set of post ids
posts=[]
for post_id in results:
    posts.append(post_id)
n_posts = 10
if(len(posts)<10):
    n_posts = len(posts)
# Extracting Comments
j=1
for i in range(n_posts):
    for comment in posts[i].comments.list():
        key = "cmnt"+str(j)
        document[key]=str(comment.body)
        j+=1
# Connection to MongoDB
client = MongoClient("mongodb+srv://coursebotadmin:Kjy5Veoukfw9Qi8F@coursedatasetcluster.v5xlc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client['CourseDataset']
coll = db['MachineLearning']
# Adding document to collection
coll.insert_one(document)
