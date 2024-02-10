from config import key
import requests #web

def chat1(chat):
    messages = [] # list which all meassages
    system_message = "you are an Ai bot your name is Jarvis " #first instruction 
    message = { "role" : "user", "parts" : [{"text": system_message +" "+ chat}]}
    messages.append(message)
    data = {" contents": meassages}
    url = ""
    response = requests.post(url, json=data)

    t1 = response.json()
    print(t1)
    t1.get("candidates")[0].get("content").get("parts")[0].get("text")


chat = "who is ms dhoni"  #pip install requests
chat1(chat) 