import requests
import time
from bs4 import BeautifulSoup
import urllib


def continue_crawl(history, target_url, max_steps=25):
    """
    indicates if we should continue crawling. will stop if
    1) our search is too deep
    2) we find our target
    3) we detect a loop
    :param history:
    :param target_url:
    :param max_steps:
    :return:
    """
    if len(history) > max_steps:
        print("stopping because we're too deep")
        return False

    if history[-1] == target_url:
        print("stopping because we found our target")
        return False

    if len(history) != len(set(history)):
        print("stopping because we're in a loop")
        return False

    return True


def find_first_link(url):
    """
    download html of the provided article
    find the first link in that html
    :param url:
    :return: first link as a string, or None if there is no link
    """
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    link1 = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return link1


start_url = 'https://en.wikipedia.org/wiki/Special:Random'
#start_url = 'https://en.wikipedia.org/wiki/Doughnut'

target_url = 'https://en.wikipedia.org/wiki/Philosophy'
article_chain = [start_url]

while continue_crawl(article_chain, target_url, 50):
    article = article_chain[-1]
    print(article)
    first_link = find_first_link(article)

    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    # add the first link to article_chain
    article_chain.append(first_link)

    # delay for about two seconds
    time.sleep(1)
