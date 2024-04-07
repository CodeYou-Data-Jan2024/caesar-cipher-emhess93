alphabet_dict = {"a":"f", "b":"g", "c":"h", "d":"i", "e":"j", "f":"k", "g":"l", "h":"m", "i":"n", "j":"o", "k":"p", "l":"q", "m":"r", "n":"s", "o":"t", "p":"u", "q":"v", "r":"w", "s":"x", "t":"y", "u":"z", "v":"a", "w":"b", "x":"c", "y":"d", "z":"e"}

#ask for user input
sentence = input("Enter a sentence: ")

#create lower case list of words
sentence = sentence.lower()

new_sent = ""

for letter in range(0, len(sentence)):
    new_sent = new_sent + (alphabet_dict.get(sentence[letter], sentence[letter]))
print(new_sent)

