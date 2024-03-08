#news_app_using_https://newsapi.org/_as(API)
import requests
import json
import time

def greeting():
    timestamp = time.strftime("%H:%M:%S")
    print(timestamp)
    timestamp_H = int(time.strftime("%H"))
    # timestamp_H = int(input("Time_ "))
    if (20< timestamp_H or timestamp_H <=4):
        print("Hola,./!#,.")
    elif (16< timestamp_H <=20):
        print("Hola, Good Evening")
    elif (11< timestamp_H <=16):
        print("Hola, Good Afternoon")
    elif (4< timestamp_H <=11):
        print("Hola,Good Morning")


greeting()
while True:
    query = input("What type of news are you interested in?\n:")
    if query == "quit()":
        print("NEwS aPP -_-")
        break
    else:
        url = f"https://newsapi.org/v2/everything?q={query}&from=2024-02-08&sortBy=publishedAt&apiKey=adb22056534f4f10b95262a9cfe113d8"
        r = requests.get(url)
        news = json.loads(r.text)
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("=======")
        print("type quit() to exit")
