# creating a class as sample
class sample:
    a = "virat"


obj = sample()
obj.a = "vishal"

print(sample.a)
print(obj.a)

# it does not change class attribute



# while changing class attribute-->
class sample:
    a = "virat"


obj = sample()

sample.a = "vishal"

print(sample.a)
print(obj.a)

