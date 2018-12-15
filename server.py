# -*- coding: utf-8 -*-


#%%
from flask import Flask, jsonify

Tooter = {
        "Tan":["Dani","Alejandro"],
        "Zineb":["Tan","Alejandro"],
        "Alejandro":["Tan","Alejandro"],
        "Dani":[]
        }

Toots =  {
        "Tan":["Hello World"],
        "Zineb":["#Peace&Love"],
        "Alejandro":["Hello to my Fans"],
        "Dani":["Follow for Follow!!!!"]
        }

#We assume that this will be impemented on an actual HTML page trough buttons, 
#hence you can only follow users that have a page /exist, as otherwise there 
#woudlnt be a webpage with a follow button"


server = Flask("Tooter server ")

@server.route("/hello")
def hello_handler():
    return jsonify({"message":"Hello to Tooter"})


#GET THE TIMELINE
@server.route("/user/<username>/timeline")
def user_handler(username):
   Tooters_toots=[]
   for i in Tooter[username]:
       dicti = {"toots":Toots[i],"user":i}
       Tooters_toots.append(dicti)
   timeline = {"My toots" : Toots[username],"Followers Toots":Tooters_toots}
   return jsonify(timeline)

#CREATE A TOOT 
    
@server.route("/createtoot/<username>/<toot>", methods=["POST"])
def create_toots(username,toot):
    Toots[username].append(toot)
    return jsonify({"message":"Toot created!","username":username, "toot":toot})

#FOLLOW OTHER USERS

@server.route("/<me>/follow/<username>", methods=["POST"])
def follow(me,username):
    Tooter[me].append(username)
    return jsonify({"message":"Followed!", "username":username})

#UNFOLLOW
@server.route("/<me>/unfollow/<username>", methods=["POST"])
def unfollow(me,username):
    Tooter[me].remove(username)
    return jsonify({"message":"Unfollowed!", "username":username})



server.run()