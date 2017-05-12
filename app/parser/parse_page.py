import urllib
from bs4 import BeautifulSoup
       

def get_users(base_url,pageN):
#get users by post id, from all post on page
    p = urllib.urlopen(base_url + str(pageN)).read()
    soup = BeautifulSoup(p, "html.parser")
    users_by_ids = tuple()
    
    for tag in soup.body.find_all('td', class_='subtext'):
        subtext_data = {}   
        subtext_id = None
        autor = ''   
        
        for age_tag in tag.find_all('span', class_='age'):
            age_link =  age_tag.find('a').get('href')
            subtext_id = age_link[age_link.rfind('?id=')+4:]
            
        for user_tag in tag.find_all('a', class_='hnuser'):
                autor = user_tag.contents[0]
        
        subtext_data[int(subtext_id)] = autor
        
        users_by_ids += (subtext_data, )
    return  users_by_ids


def parse_page(base_url, pageN, itemsN):


    def ckeck_empty_tag(tag_element):
        if not isinstance(tag_element, type(None)):
            return tag_element.text
        else:           
            return 'empty'


    p = urllib.urlopen(base_url + str(pageN)).read()
    soup = BeautifulSoup(p, "html.parser")
    page_posts = tuple()
    #fetch by 'athing'  row
    post_items_l = soup.body.find_all('tr', class_='athing') 
    for c, row in enumerate(post_items_l):
        #stop fetching page, when need few posts last page
        if c >= itemsN:
            break
        #define post dictionary structure for post
        post = dict()
        
        post['post_id'] = int(row.get('id', 0))
        post['url'] = row.find('a', class_='storylink').get('href','empty')
        post['title'] = ckeck_empty_tag(row.find('a', class_='storylink'))
        post['site'] = ckeck_empty_tag(row.find("span", class_="sitestr"))
        
        for user in get_users(base_url,pageN):
            if post['post_id']  in  user.keys():
                post['autor'] =  user.get((post['post_id']),'')       
        page_posts += (post, )                
    
    return page_posts
        