color = ["black", "brown", "red", "orange", "yellow", "green", "blue","violet","grey","white"]
c1 = input()
c2 = input()
c3 = input()
print(((color.index(c1)*10) + color.index(c2)) * (10 ** color.index(c3)))