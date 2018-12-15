#%%
import requests

localhost = "http://127.0.0.1:5000"

# GET TIMELINE - DONE
def get_timeline(user):
    response = requests.get(localhost+"/user/"+user+"/timeline")
    if response.status_code == 200:
        return response.json() 
    else:
        return response.status_code
    
#Create toot     
def create_toot(user,toot):
    response = requests.post(localhost+"/createtoot/"+user+"/"+toot)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code  

#Unfollow 
        
def unfollow_tooter(me,username):
    response = requests.post(localhost + "/"+ me +"/unfollow/"+username)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code   

#Follow
def follow_tooter(me,username):
    response = requests.post(localhost + "/"+ me +"/follow/"+username)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code   




        
        

        

        
        