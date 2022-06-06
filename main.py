l1 =['0','1','2','3','4','5','6','7','8']
l2 =['0','1','2','3','4','5','6','7','8']
l3 =['0','1','2','3','4','5','6','7','8']

#Defining Functions:

def printABC():
    print(f'''A      B      C
{l1[0]} {l1[1]} {l1[2]}  {l2[0]} {l2[1]} {l2[2]}  {l3[0]} {l3[1]} {l3[2]}
{l1[3]} {l1[4]} {l1[5]}  {l2[3]} {l2[4]} {l2[5]}  {l3[3]} {l3[4]} {l3[5]}
{l1[6]} {l1[7]} {l1[8]}  {l2[6]} {l2[7]} {l2[8]}  {l3[6]} {l3[7]} {l3[8]}''')
def printAB():
    print(f'''A      B
{l1[0]} {l1[1]} {l1[2]}  {l2[0]} {l2[1]} {l2[2]}
{l1[3]} {l1[4]} {l1[5]}  {l2[3]} {l2[4]} {l2[5]}
{l1[6]} {l1[7]} {l1[8]}  {l2[6]} {l2[7]} {l2[8]}''')
def printBC() :
    print(f'''B      C
{l2[0]} {l2[1]} {l2[2]}  {l3[0]} {l3[1]} {l3[2]}
{l2[3]} {l2[4]} {l2[5]}  {l3[3]} {l3[4]} {l3[5]}
{l2[6]} {l2[7]} {l2[8]}  {l3[6]} {l3[7]} {l3[8]}''')
def printAC():
    print(f'''A      C
{l1[0]} {l1[1]} {l1[2]}  {l3[0]} {l3[1]} {l3[2]}
{l1[3]} {l1[4]} {l1[5]}  {l3[3]} {l3[4]} {l3[5]}
{l1[6]} {l1[7]} {l1[8]}  {l3[6]} {l3[7]} {l3[8]}''')
def printA():
    print(f'''A
{l1[0]} {l1[1]} {l1[2]}
{l1[3]} {l1[4]} {l1[5]}
{l1[6]} {l1[7]} {l1[8]}''')
def printB():
    print(f'''B
{l2[0]} {l2[1]} {l2[2]}
{l2[3]} {l2[4]} {l2[5]}
{l2[6]} {l2[7]} {l2[8]}''')
def printC():
    print(f'''C
{l3[0]} {l3[1]} {l3[2]}
{l3[3]} {l3[4]} {l3[5]}
{l3[6]} {l3[7]} {l3[8]}''')
a = 'A2'
printABC()
x = 0
y = 0 
z = 0
def checkingA():
    global x
    x = 0

    if l1[0] == 'X' and l1[1] == 'X' and l1[2] == 'X' :
        x += 1

    elif l1[3] == 'X' and l1[4] == 'X' and l1[5] == 'X' :
        x += 1
    elif l1[6] == 'X' and l1[7] == 'X' and l1[8] == 'X' :
        x += 1
    elif l1[0] == 'X' and l1[3] == 'X' and l1[6] == 'X':
        x += 1 
    elif l1[1] == 'X' and l1[4] == 'X' and l1[7] == 'X':
        x += 1 
    elif l1[2] == 'X' and l1[5] == 'X' and l1[8] == 'X':
        x += 1 
    elif l1[0] == 'X' and l1[4] == 'X' and l1[8] == 'X':
        x += 1
    elif l1[2] == 'X' and l1[4] == 'X' and l1[6] == 'X':
        x += 1
    else:
        x += 0
#--
def checkingB():
    global y 
    y = 0
    if l2[0] == 'X' and l2[1] == 'X' and l2[2] == 'X' :
        y += 1
    elif l2[3] == 'X' and l2[4] == 'X' and l2[5] == 'X' :
        y += 1
    elif l2[6] == 'X' and l2[7] == 'X' and l2[8] == 'X' :
        y += 1
    elif l2[0] == 'X' and l2[3] == 'X' and l2[6] == 'X':
        y += 1
    elif l2[1] == 'X' and l2[4] == 'X' and l2[7] == 'X':
        y += 1
    elif l2[2] == 'X' and l2[5] == 'X' and l2[8] == 'X':
        y += 1
    elif l2[0] == 'X' and l2[4] == 'X' and l2[8] == 'X':
        y += 1
    elif l2[2] == 'X' and l2[4] == 'X' and l2[6] == 'X':
        y += 1
    else:
        y += 0 
#------


def checkingC():
    global z
    z = 0
    if l3[0] == 'X' and l3[1] == 'X' and l3[2] == 'X' :
        z += 1


    elif l3[3] == 'X' and l3[4] == 'X' and l3[5] == 'X' :
        z += 1

    elif l3[6] == 'X' and l3[7] == 'X' and l3[8] == 'X' :
        z += 1

    elif l3[0] == 'X' and l3[3] == 'X' and l3[6] == 'X':
        z += 1

    elif l3[1] == 'X' and l3[4] == 'X' and l3[7] == 'X':
        z += 1

    elif l3[2] == 'X' and l3[5] == 'X' and l3[8] == 'X':
        z += 1

    elif l3[0] == 'X' and l3[4] == 'X' and l3[8] == 'X':
        z += 1

    elif l3[2] == 'X' and l3[4] == 'X' and l3[6] == 'X':
        z += 1
    else:
        z += 0 
#---------

def move1(a):
    while True:
        if a[0] not in ['A','B','C'] or a[1] not in ['0','1','2','3','4','5','6','7','8']:
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'A' and l1[int(a[1])] == 'X':
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'B' and l2[int(a[1])] == 'X':
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'A' and l1[int(a[1])] == 'X':
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'C' and l3[int(a[1])] == 'X':
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'A' and x == 1:
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'B' and y == 1:
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        elif a[0] == 'C' and z == 1:
            print('Invalid move, please input again')
            a = str(input('Player 1: '))
        else :
            if a[0] == 'A':
                l1[int(a[1])] = 'X'
                break
            elif a[0] == 'B':
                l2[int(a[1])] = 'X'
                break
            elif a[0] == 'C':
                l3[int(a[1])] = 'X'
                break
def move2(b):
    while True:
        if b[0] not in ['A','B','C'] or b[1] not in ['0','1','2','3','4','5','6','7','8']:
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'A' and l1[int(b[1])] == 'X':
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'B' and l2[int(b[1])] == 'X':
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'A' and l1[int(b[1])] == 'X':
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'C' and l3[int(b[1])] == 'X':
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'A' and x == 1:
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'B' and y == 1:
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        elif b[0] == 'C' and z == 1:
            print('Invalid move, please input again')
            b = str(input('Player 2: '))
        else :
            if b[0] == 'A':
                l1[int(b[1])] = 'X'
                break
            elif b[0] == 'B':
                l2[int(b[1])] = 'X'
                break
            elif b[0] == 'C':
                l3[int(b[1])] = 'X'
                break


#---GAME STARTS-----

while True :
    a1 = str(input('Player 1: '))
    move1(a1)
    checkingA() 
    checkingB()
    checkingC()
    if x == 1 and y == 0 and z == 0:
        printBC()
    elif x == 0 and y == 1 and z == 0:
        printAC()
    elif x == 0 and y == 0 and z == 1:
        printAB()
    elif x == 0 and y == 1 and z == 1:
        printA()
    elif x == 0 and y == 0 and z == 0 :
        printABC()
    elif x == 1 and y == 0 and z == 1:
        printB()
    elif x == 1 and y == 1 and z == 0:
        printC()
    elif x == 1 and y == 1 and z == 1:
        print('Player 2 wins game')
        exit()

    b1 = str(input('Player 2: '))
    move2(b1)
    checkingA()
    checkingB()
    checkingC()
    if x == 1 and y == 0 and z == 0:
        printBC()
    elif x == 0 and y == 1 and z == 0:
        printAC()
    elif x == 0 and y == 0 and z == 1:
        printAB()
    elif x == 0 and y == 1 and z == 1:
        printA()
    elif x == 1 and y == 0 and z == 1:
        printB() 
    elif x == 0 and y == 0 and z == 0 :
        printABC()
    elif x == 1 and y == 1 and z == 0:
        printC()
    elif x == 1 and y == 1 and z == 1:
        print('Player 1 wins game')
        exit()
