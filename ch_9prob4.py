with open("sample.txt") as f:
    content = f.read()
    
    content = content.replace("Dog","#@$") 

with open("sample.txt", "w")as f:   
  f.write(content)