import json
from flask import Flask, jsonify
from parser.parser import *


save_parsed_results(run_parsing_queue()) #run parsing and save results


def open_posts():
    try:
        with open ('output.allposts', "r") as impfile:
            data = impfile.readlines()
    except (IOError, OSError):        
        data = []
        return False
    if len(data[0])>0:        
        post_data = json.loads(data[0])
        return post_data


app = Flask(__name__)


@app.route('/')
def index():
    return "Enter Point"

@app.route('/api/posts', methods=['GET'])
def get_all_post(): 
    posts = open_posts()    
    return jsonify({'posts': posts})
    

@app.route('/api/posts/:<site>', methods=['GET'])
def get_posts_by_site(site): 
    posts = open_posts() 
    posts_filtered = []
    for post in posts:
        if site == post.get('site', ""):
            posts_filtered.append(post)
    return jsonify({'posts': posts_filtered})


if __name__ == '__main__':    
    app.run()