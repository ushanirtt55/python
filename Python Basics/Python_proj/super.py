class Thought(object):
    def __init__(self):
        pass
    def message(self):
        print "I feel like I am diagonally parked in a parallel universe."
 
class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()
    def message(self):
        print "Warning: Dates in calendar are closer than they appear"
        super(Advice, self).message()

