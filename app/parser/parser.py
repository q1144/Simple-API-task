import urllib, Queue, json
from bs4 import BeautifulSoup

from page_queue import build_page_data
from parse_page import parse_page


def run_parsing_queue():
    #Set enter point for parsing
    BASEURL = "https://news.ycombinator.com/news?p="
    ALL_POSTS = []

    q = Queue.Queue()
    #insert pages to the queue
    for item in build_page_data(BASEURL):
        q.put(item)
        
    while not q.empty():
        q_item = q.get()
        ALL_POSTS += parse_page(BASEURL, q_item['num'], q_item['posts'])

    return ALL_POSTS
    

def save_parsed_results (results):
    with open("output.allposts", "w") as text_file:
        text_file.write(json.dumps(results) )
    return True
    