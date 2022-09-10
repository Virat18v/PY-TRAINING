text = input("enter the text\n")
if("make a lot of money" in text):
    spam = true
elif("buy now" in text):
    spam = true
elif("click this" in text):
    spam = true
elif("subscribe this " in text):
    spam = true
else:
    spam = false
if(spam):
 print("this text is spam")
else:
 print("this text is not spam")
  