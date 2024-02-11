import requests


def temp_cites(city):
    
    url = "https://yahoo-weather5.p.rapidapi.com/weather"  #endpoint 

    querystring = {"location":"sunnyvale","format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())


print(temp_cites("delhi"))