f=open('poems.txt')
t=f.read()
if 'twinkle'in t:
    print("Twinkle is present")
else:
    print("twinkle is not present")
f.close()