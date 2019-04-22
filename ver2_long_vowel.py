#Long-vowels Exercise version 2

sentence = input("Please create a sentence: ")
new_sentence = ''

for letter in sentence:
    if ("a" == letter):
        new_sentence += ("a" * 5)
    elif ("e" == letter):
        new_sentence += ("e" * 5)
    elif ("i" == letter):
        new_sentence += ("i" * 5)
    elif ("o" == letter):
        new_sentence += ("o" * 5)
    elif ("u" == letter):
        new_sentence += ("u" * 5)
    else:
        new_sentence += letter

print(new_sentence)