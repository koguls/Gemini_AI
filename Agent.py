#this file execue the reprective fuction based on user query
import Task-Temp.py


def conversation(user_message, messages):
    messages = [] # list which all meassages
    system_message = "you are an Ai bot your name is Jarvis " #first instruction 
    
    message = { "role" : "user", 
               "parts" : [{"text": system_message +"\n "+ user_message}]}
    
    messages.append(message)

    data = {"contents": [meassages], 
            "tools" :
            [ { "fuctionDeclarations" : Task-Temp.definitions

            }]
            }
    url = ""
    response = requests.post(url, json=data)

    if response.status != 200:
        print(response.text)

    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("error : no conent")
    #print(t1)
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)