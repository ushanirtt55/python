def make_acronym(phrase):
    a=[ ''.join(word[0].upper)  if word.isalpha() else 0  for word in phrase ]
    print a
    
a=make_acronym('hel1o world')