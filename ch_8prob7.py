#funciton to remove a given word from string
def remove_and_split(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

this ="   virat is a good   "
n = remove_and_split(this, "virat")
print(n)

    