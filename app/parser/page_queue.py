import urllib
from bs4 import BeautifulSoup


def build_page_data(URL):
    pages = tuple()
    #init counters 
    posts_counter = 0
    page_num = 1

    while posts_counter < 100:
        p = urllib.urlopen(URL+ str(page_num)).read()
        soup = BeautifulSoup(p, "html.parser")
        #init inside loop variables:
        page_info=dict()  
        posts_on_page = 0
        
        posts_on_page += len(soup.body.find_all('tr', class_='athing'))
        posts_counter += posts_on_page  
        
        if posts_counter > 100:       #Handle last page case, due to max lenght = 100
            posts_on_page = 100-(posts_counter-posts_on_page) 
    
        page_info['num'] = page_num
        page_info['posts'] = posts_on_page
        #put dict page to the queue 
        page_num +=1
        pages += (page_info, )
        
    return pages   