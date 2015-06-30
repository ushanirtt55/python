import itertools
annograms = lambda word: map(lambda c: ''.join(c),
                             set(itertools.permutations(word)).intersection(
                               tuple(w.rstrip()) for w in open('/home/umashankar/Downloads/WORD.LST')))
print annograms('Test')