#14.Reverse word program

def reverse_words(sentence):
 words= sentence.split()
 reversed_words = words[::-1]
 return " ".join (reversed_words)

# Test
print(reverse_words("pythone is easy to learn")) 