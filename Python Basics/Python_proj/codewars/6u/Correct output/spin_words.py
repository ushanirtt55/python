def spin_word(sentence):
    lis=' '.join (w[::-1] if len(w)>=5 else w for w in sentence.split(' '))
    print lis
            
spin_word("elbuod decaps sdrow")