n = int(input())
light = [620,590,570,495,450,425,380]
color = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
for i in range(len(light)):
    if n >= light[i]:
        print(color[i])
        break