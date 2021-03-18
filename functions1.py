def findArea(a, b):
    area = a*b**2
    # print(area)
    return area

pi = 3.14
r = 5

print(findArea(pi,r))

#%%
class Animal(object):
    def __init__(self, a, b):
        self.name = a
        self.age = b
    def getName(self):
        #print(self.name)
        return self.name
    def getAge(self):
        #print(self.age)
        return self.age

a1 = Animal("dog", 2)
print(a1.getName() and a1.getAge())
a2 = Animal("cat", 3)
a3 = Animal("fish", 1)
# %%
