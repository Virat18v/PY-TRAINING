words = ["apple", "mango", "guava"]

with open("sample2.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "######")
    with open("sample2.txt", "w") as f:
        f.write(content)