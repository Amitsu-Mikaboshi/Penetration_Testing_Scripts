import click
import requests
import re
from bs4 import BeautifulSoup

'''Request module amader provide kora url er source code fetch korbe and output e content dibe'''
def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'HTTP status code of {resp.status_code} returned, but 200 was expected. Exiting...')
        exit(1)

    return resp.content.decode()

'''Ekhane amader provide kora wordlist er length onujai count korte thakbe tara kotobar appear hocche. By default minimum length zero thakbe. Means sob
word included thakbe, jodi amra special criteria set nh kori. And ai functioner output hobe list theke pawa word gulor appearance count kore akta dictionary
banano'''
def count_occurrences_in(word_list, min_length):
    word_count = {}

    for word in word_list:
        if len(word) < min_length:
            continue
        if word not in word_count:
            word_count[word] = 1
        else:
            current_count = word_count.get(word)
            word_count[word] = current_count + 1
    return word_count

'''Ei function tah kaj korbe request module theke pawa content er upor. setake beautifulSoup diye sundor vhabe align kora and then interact kora
ei function er main kaj hocche source code theke tag bade baki string gulo collect kora then pawa string gulo ke word hisabe alada kora and output e generate
kora. Means ekhane amra content er sob word er akta list pabo'''
def get_all_words_from(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

'''Ekhane amra top occurance er upor base kore akta sort list pabo word er. Aita generally word count function ke call korbe and tar output dictionary 
ke use kore akta sorted dictionary generate korbe output hisabe'''
def get_top_words_from(all_words, min_length):
    occurrences = count_occurrences_in(all_words, min_length)
    return sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

'''Ekhane amader flag hisabe input neowar main kaj hobe and amra sei input guloke main e pass korbo. Jehetu main e pass kora hoise tahole main function ke
explicitly call kora lagbe. tai ekhane Python Idiom use kora mendatory jekhane main function ke call kora hobe'''
@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length (default: 0, no limit).')
def main(url, length):
    the_words = get_all_words_from(url)
    top_words = get_top_words_from(the_words, length)

    for i in range(10):
        print(top_words[i][0])

if __name__ == '__main__': # Eita must be use korte hobe. kenona aita use nh korle main function kokhonoi call hobe nh and rest of the kaj unsolve thakbe
    main()