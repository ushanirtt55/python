import os
from gitdb.util import dirname

print os.path.join("/home/umashankar/Downloads/Test", "263-Talented.doc")
print os.path.expanduser("~")
dirname="/home/umashankar/Downloads"

for i in os.listdir(dirname):
    print i
