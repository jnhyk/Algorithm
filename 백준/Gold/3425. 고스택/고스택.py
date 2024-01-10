go = ["NUM", "POP", "INV", "DUP", "SWP", "ADD","SUB","MUL","DIV","MOD"]
q = 1
while(q):
    ins = []
    num = []
    v = []
    while(1):
        I = input()
        if I == "":
            continue
        if I == "QUIT":
            q = 0
            break
        if I == "END":
            break
        elif len(I) > 3:
            num.append(int(I[4:]))
            I = I[:3]
        ins.append(I)
    if q == 0:
        break
    n = int(input())
    for _ in range(n):
        number = 0
        i = []
        i.append(int(input()))
        for j in range(len(ins)):
            if ins[j] == go[0]:
                i.append(num[number])
                number += 1
            elif ins[j] == go[1]:
                if len(i) == 0:
                    i = []
                    break
                i.pop()
            elif ins[j] == go[2]:
                if len(i) == 0:
                    i = []
                    break
                i[-1] = - i[-1]
            elif ins[j] == go[3]:
                if len(i) == 0:
                    i = []
                    break
                i.append(i[-1])
            elif ins[j] == go[4]:
                if len(i) < 2:
                    i = []
                    break
                i[-1],i[-2] = i[-2],i[-1]
            elif ins[j] == go[5]:
                if len(i) < 2:
                    i = []
                    break
                o1 = i.pop()
                o2 = i.pop()
                if abs(o2 + o1) > 10**9:
                    i = []
                    break
                i.append(o2+o1)
            elif ins[j] == go[6]:
                if len(i) < 2:
                    i = []
                    break
                o1 = i.pop()
                o2 = i.pop()
                if abs(o2 - o1) > 10**9:
                    i = []
                    break
                i.append(o2-o1)
            elif ins[j] == go[7]:
                if len(i) < 2:
                    i = []
                    break
                o1 = i.pop()
                o2 = i.pop()
                if abs(o2 * o1) > 10**9:
                    i = []
                    break
                i.append(o2*o1)
            elif ins[j] == go[8]:
                if len(i) < 2:
                    i = []
                    break
                o1 = i.pop()
                o2 = i.pop()
                if o1 == 0:
                    i = []
                    break
                if (o2 < 0 and o1 > 0) or (o2 > 0 and o1 < 0):
                    o2 = abs(o2)
                    o1 = abs(o1)
                    i.append(-(o2//o1))
                else: 
                    i.append(o2//o1)
            else:
                if len(i) < 2:
                    i = []
                    break
                o1 = i.pop()
                o2 = i.pop()
                if o1 == 0:
                    i = []
                    break
                if o2 < 0:
                    o2 = abs(o2)
                    o1 = abs(o1)
                    i.append(-(o2%o1))
                else: 
                    o2 = abs(o2)
                    o1 = abs(o1)
                    i.append(o2%o1)
        if len(i) != 1:
            v.append("ERROR")
            continue
        v.append(i.pop())

    for i in v:
        print(i)
    print()
    

