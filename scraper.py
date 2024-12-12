import requests
from bs4 import BeautifulSoup
import json

def scrape():
    url = "https://a16z.com/"
    # response object. Here are SOME of its attributes:
    # response.status_code : 200 for success, 404 for not found, 500 for server error
    # response.headers : info sent by client to the server to provide information about request
    # response.text : raw response content as a string 
    # response.content : raw response content in bytes
    # response.json : parses response content as a JSON and returns a dictionary
    response = requests.get(url)
    # print(response.text)

    # BeautifulSoup parses HTML content
    content = BeautifulSoup(response.content, 'html.parser')
    # print(content)

    page_text = []
    for text in content.find_all('div', attrs={"class": "home-intro data-content-on-scroll"}):
        # print(text.attrs)
        page_text.append(text.text)
    
    for section in page_text:
        print(section, "\n")


if __name__ == "__main__":
    scrape()

