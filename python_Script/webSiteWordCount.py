import requests
import re
from bs4 import BeautifulSoup

PAGE_URL = 'http://target:port' #We need to change this according to the attack website port. Just use nmap to find a port where apacahe or similar type of
# server works. Once I get it. then I can fetch data in that webApp

def get_html_of(url): # this function will get the url and then check if the page is alive or not. Considering the OK status code is my main concern.
    # response other than that would not consider as a function to use
    resp = requests.get(url) # request module is resposible for fetching webpage source code

    if resp.status_code != 200: # this is the checker line. That indicated we only accept the OK status code
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

html = get_html_of(PAGE_URL)
soup = BeautifulSoup(html, 'html.parser') # beautifulSoup is used to interact with the fetch source code
raw_text = soup.get_text() # this will remove the tags and only fetch strings from the source code
all_words = re.findall(r'\w+', raw_text) # it will make a list of words from the strings data we fetch earlier 

word_count = {} 

for word in all_words: # this function is responsible for filter out the unique word and count them accordingly
    if word not in word_count:
        word_count[word] = 1
    else:
        current_count = word_count.get(word)
        word_count[word] = current_count + 1

top_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True) # this will sort out the word list depend on maximum used word

for i in range(10): # this loop will run 10 times means it will print top 10 most used word
    print(top_words[i]) # as top_words is a tuple , so it will print key along with its value. Means we will have the word along with its occurance


# this is the basic of web scraping. Beiginner may face some issue. Again this is my way of coding . So maybe it will not suit or may conflict with others 
# styling or syntex of coding. Again python does not mind styling. So feel free to build your own. 