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
        print(text.attrs)
        # page_text.append(text.text)
    
    # for section in page_text:
    #     print(section, "\n")

# <p style="translate: none; rotate: none; scale: none; transform: translate(0px, 0px); opacity: 1;">Andreessen Horowitz (aka a16z) is a venture capital firm that backs bold entrepreneurs <a class="link-decor" href="/news-content">building the future</a> through technology. We are&nbsp;<a class="link-decor" href="/portfolio">stage agnostic</a>. We invest in seed to venture to <a class="link-decor" href="/growth/">growth-stage technology</a> companies, across <a class="link-decor" href="https://a16z.com/ai/">AI</a>, <a class="link-decor" href="/bio-health/">bio&nbsp;+&nbsp;healthcare</a>, <a class="link-decor" href="/consumer/">consumer</a>, <a class="link-decor" href="https://a16zcrypto.com/">crypto</a>, <a class="link-decor" href="/enterprise/">enterprise</a>, <a class="link-decor" href="/fintech/">fintech</a>, <a class="link-decor" href="/games">games</a>, <a class="link-decor" href="https://a16z.com/infra/">infrastructure</a>, and companies building toward <a class="link-decor" href="/american-dynamism/">American dynamism</a>. a16z has $44B in committed capital across multiple funds.</p>

if __name__ == "__main__":
    scrape()

