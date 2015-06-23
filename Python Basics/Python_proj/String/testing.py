import string

a=string.maketrans('abcdefj', '1234567')
s = 'The quick brown fox jumped over the lazy dog.'
print s.translate(a)