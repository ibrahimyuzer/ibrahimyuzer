a = ["a","b","c"]

print("a" in a)
print("d" in a)

#%%
carpim = 1
liste = [1,2,3,4,5]

for i in liste:
    carpim = carpim * i
    print(carpim)

toplam = 0
liste1 = [1,2,3,4,5,6,7,8,9]
for i in liste1:
    toplam = toplam + i
    print(toplam)

for i in liste1:
    if i % 2 == 1:
        print(i)
for i in liste1:
    if i % 2 == 0:
        print(i)

a = "ibrahim"
for i in a:
    print(i)

liste2 = [1,2,3,4,5]
for i in liste2:
    print(i*3)

demet = (1,2,3,4,5)
for a in demet:
    print(a)

liste3 = [(1,2,3),(4,5,6),(7,8,9)]
for a in liste3:
    print(a)

for a,b,c in liste3:
    print(a,b,c)
for a,b,c in liste3:
    print("a {} b {} c {}".format(a,b,c))