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
leaders = [
        'Narendra Modi', 'Donald Trump', 'Joe Biden', 'Rahul Gandhi', 'Jacinda Ardern', 'Justin Trudeau', 'Boris Johnson', 'Scott Morrison', 'Xi Jinping', 'Mette Frederiksen',
        'Sanna Marin', 'Emmanuel Macron', 'Olaf Scholz', 'Naftali Bennett', 'Fumio Kishida', 'Alihan Smaiylov', 'Uhuru Kenyatta', 'Muhammadu Buhari', 'Kim Jong-un', 
        'Haitham bin Tariq', 'Shehbaz Sharif', 'Imran Khan', 'Mahmoud Abbas', 'Bongbong Marcus', 'Vladimir Putin', 'Salman bin Abdulaziz Al Saud', 'Macky Sall', 
        'Lee Hsien Loong', 'Mohamed Hussien Roble', 'Mahinda Rajapaksa', 'Gotabaya Rajapaksa', 'Salva Kiir Mayardit', 'Yoon Suk-yeol', 'Cyril Ramaphosa', 
        'Abdel Fattah al-Burhan', 'Magdalena Andersson', 'Ignazio Cassis', 'Bashar al-Assad', 'Emmerson Mnangagwa', 'Sheikh Khalifa bin Zayed Al Nahyan', 'Volodymyr Zelenskyy',
        'Abraham Lincoln', 'Nelson Mandela', 'A.P.J. Abdul Kalam', 'Kofi Annan', 'Aung San Suu Kyi', 'Atal Bihari Vajpayee', 'Jawaharlal Nehru', 'Robert Mugabe', 'Ashraf Ghani'
        ]
#for leader in leaders :
for i in range(41,50,1):
    leader = leaders[i]
    document = {}
    results = reddit.subreddit("all").search(leader)
    document["title"] = leader
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
        #x=1
        posts[i].comments.replace_more(limit=0)
        cmnt_lst = posts[i].comments.list();
        print(cmnt_lst)
        for comment in cmnt_lst:
            key = "cmnt"+str(j)
            document[key]=str(comment.body)
            j+=1
    # Connection to MongoDB
    client = MongoClient("mongodb+srv://l3admin:JZlYHY7fumfjrjQg@l3dataset.v5xlc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    db = client['L3Dataset']
    coll = db['Leaders']
    # Adding document to collection
    coll.insert_one(document)
