class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index}  +"
            index += 1
            return str1[:-1]

        def _add_(self, vec2):
            newList = []
            for i in range(len(self.vec)):
                newList.append(self.vec[i] + vec2.vec[i])
                return vector(newList)


v1 = vector([7, 2, 4])
v2 = vector([8, 3, 1])
print(v1)
print(v1+v2)
