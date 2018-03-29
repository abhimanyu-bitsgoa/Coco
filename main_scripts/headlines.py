import requests, json
from termcolor import colored
from unidecode import unidecode


def getHeadlines(source):
    source="google-news-in"
    newsSource =source
    url = "https://newsapi.org/v2/top-headlines?apiKey=2ff80ad49a294ffc88827b9f0b47cb6c&sources=" + newsSource
    response = requests.get(url)
    data = response.json()
    if data["status"] != "error":
        articles = data["articles"]
        for article in articles:
            print(colored(unidecode(article["title"]),'green'))
            if article["description"] is not None:
                print(unidecode(article["description"]))
                print(colored(article["url"],'yellow'))
                print(" ")
    else:
        print("Invalid news source.")

if __name__ == '__main__':
    getHeadlines("google-news-in")
