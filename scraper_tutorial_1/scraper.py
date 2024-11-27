# library to send HTTP requests and fetch content from a webpage
import requests
# library used to parse and extract structured data from HTML documents
from bs4 import BeautifulSoup
import json
import os

def scrape():
    url = "http://ethans_fake_twitter_site.surge.sh/"
    response = requests.get(url)
    content = BeautifulSoup(response.content, 'html.parser')

    # tweet = content.findAll('p', attrs={"class": "content"})
    tweetArr = []
    for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
        tweetObject = {"author": tweet.find('h2', attrs={"class": "author"}).text, 
                       "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
                       "tweet": tweet.find('p', attrs={"class": "content"}).text, 
                       "likes": tweet.find('p', attrs={"class": "likes"}).text,
                       "shares": tweet.find('p', attrs={"class": "shares"}).text}
        tweetArr.append(tweetObject)

    json_file = "twitterData.json"
    with open(json_file, 'w') as outfile:
        json.dump(tweetArr, outfile)

def parse_json():
    json_file = "twitterData.json"
    with open(json_file) as json_data:
        jsonData = json.load(json_data)
        for i in jsonData:
            if "trump" in i["tweet"].lower():
                print(i)

if __name__ == '__main__':
    # scrape()
    parse_json()