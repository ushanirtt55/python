"""def disemvowel(string):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    
    str=''.join([x for x in string if x not in vowels])
    print str
"""
"""def disemvowel(string):
    newstr = string.lower()
    vowels = ('a', 'e', 'i', 'o', 'u')    
    for x in newstr:
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr
"""
def disemvowel(s):
    print s.translate(None, "aeiouAEIOU")
a= disemvowel("This website is for losers LOOOOL!")

