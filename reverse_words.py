#To reverse the words backwards

paragraph = ("This is my paragraph. I like ice cream.")
new_par= paragraph.split()
counter = 0

while counter <= len(new_par):
    print(new_par[counter -1])
    counter -= 1