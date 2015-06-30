import facebook

token = '1596640560604815|fYj1Nglkwvh_uMkEZCSImxNjeR4'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list