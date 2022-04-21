import math
import random


nomore = []
A1 = int(input("A1: "))
nomore.append(A1)
while True:
    A2 = int(input("A2: "))
    if A2 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(A2)
        break
while True:
    A3 = int(input("A3: "))
    if A3 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(A3)
        break
while True:
    B1 = int(input("B1: "))
    if B1 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(B1)
        break
while True:
    B2 = int(input("B2: "))
    if B2 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(B2)
        break
while True:
    B3 = int(input("B3: "))
    if B3 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(B3)
        break
while True:
    C1 = int(input("C1: "))
    if C1 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(C1)
        break
while True:
    C2 = int(input("C2: "))
    if C2 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(C2)
        break
while True:
    C3 = int(input("C3: "))
    if C3 in nomore:
        print("Don't repeat any number")
    else:
        nomore.append(C3)
        break
numbers = [1,2,3,4,5,6,7,8,9]
def board():
    print("BOARD:")
    print(str(A3) + " " + str(B3) + " " + str(C3))
    print(str(A2) + " " + str(B2) + " " + str(C2))
    print(str(A1) + " " + str(B1) + " " + str(C1))
board()
print("REMINDER: Algorithm doesn't use the information of the board it guesses the numbers itself")
print("Hint 1")

# How to Get the 3 Addends
sum = int(input("What is C+ Equal to? "))
dep = 1
add1 = 1
amount = 0
while True:
    add1 += 1
    if add1 == dep:
        add1 += 1
    add2 = sum - dep - add1
    if add1 != add2 and dep != add1 and dep != add2 and add2 > 0 and dep < 10 and add1 < 10 and add2 < 10:
        output = str(dep) + " + " + str(add1) + " + " + str(add2)
        amount += 1
        print(output)
    if sum - dep < 4:
        # This is the contionuation
        if dep < 10:
            spec = str(dep) + " + " + str(add2) + " + " + str(add1)
            amount += 1
            print(spec)
        print(str(amount) + " results founded")
        print(str(amount) + " options give us approximately " + str(math.floor(100 / amount)) + "% data")
        board()
        run = input("ok working")
        break
    if sum - add1 < 4:
        dep += 1
        add1 = 0

# Some Useless Staff

# How to Get the 2 Addends
"""
sum = 150
n = 1
nomore = []
while True:
    x = sum - n
    print(str(x) + " + " + str(n))
    n += 1
    if n == 150:
        break 

def addends():
    # How to Get the 3 Addends
    sum = int(input(": "))
    dep = 1
    add1 = 1
    amount = 0
    while True:
        add1 += 1
        if add1 == dep:
            add1 += 1
        add2 = sum - dep - add1
        if add1 != add2 and dep != add1 and dep != add2 and add2 > 0 and dep < 10 and add1 < 10 and add2 < 10:
            output = str(dep) + " + " + str(add1) + " + " + str(add2)
            amount += 1
            print(output)
        if sum - dep < 4:
        # This is the contionuation
            if dep < 10:
                spec = str(dep) + " + " + str(add2) + " + " + str(add1)
                amount += 1
                print(spec)
            print(str(amount) + " results founded")
            print(str(amount) + " options give us approximately " + str(math.floor(100/amount)) + "% data")
            break
        if sum - add1 < 4:
            dep += 1
            add1 = 0

addends() """
def product():
    flag = False
    # Get the 3 Factors
    product = int(input(": "))
    for d in range(2, int(product /2 + 1)):
        if product % d == 0:
            flag = True
            break
    if flag:
        for i in range(1, product + 1):
            if product % i == 0:
                print(i)
    else:
        print("prime number has no deal here")

# Subtraction
def sub():
    subtract = int(input(": "))
    sub1 = 1
    deps = 9
    while True:
        sub2 = deps - sub1 - subtract
        if subtract > 6:
            print("C- can't have that value")
            break
        if subtract < -16:
            print("C- can't have that value")
            break
        if subtract < - 6:
            pass
            # Note that minimum value for deps to get (C- = -7; -8) is 8  if (C- = -9; -10) deps is 7
            # Remember that the starter value for C- is always odd
        if subtract == -7 or subtract == -8:
            deps == deps - 1
            print(subtract)
            print(deps)
        print(deps)
        break


sub()





