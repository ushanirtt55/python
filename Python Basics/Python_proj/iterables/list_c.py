

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print words
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print word_lengths
        