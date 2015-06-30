import facebook
import requests
 
def some_action(post):
    print post['Hello Test']
    print "----------------------------------------------------"
 
access_token = '1596640560604815|fYj1Nglkwvh_uMkEZCSImxNjeR4'
graph = facebook.GraphAPI(access_token)
posts = graph.get_connections('uplbconfessions', 'posts',limit=15)
while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break