
def reverse_words(sentence):
    lis=' '.join (w[::-1] for w in sentence.split(' '))
    print lis
            
reverse_words("elbuod decaps sdrow")