C = 15
G = 100
Fr = 1100
M = 12000
Fc = 130000
B = 1400000
T = 20000000
W = 330000000
S = 5100000000
AL = 75000000000
Po = 1000000000000
TM = 14000000000000
AC = 170000000000000
Pr = 2100000000000
Ch = 26000000000000
FE = 310000000000000
JC = 71000000000000000
Iv = 12000000000000000000
CB = 1900000000000000000000
Y = 540000000000000000000

last_result = 0

while True:
    tower = input("Please input tower abbreviation: ")
    if tower == "C":
        x = C
    elif tower == "G":
        x = G
    elif tower == "Fr":
        x = Fr
    elif tower == "M":
        x = M
    elif tower == "Fc":
        x = Fc
    elif tower == "B":
        x = B
    elif tower == "T":
        x = T
    elif tower == "W":
        x = W
    elif tower == "S":
        x = S
    elif tower == "AL":
        x = AL
    elif tower == "Po":
        x = Po
    elif tower == "TM":
        x = TM
    elif tower == "AC":
        x = AC
    elif tower == "Pr":
        x = Pr
    elif tower == "Ch":
        x = Ch
    elif tower == "FE":
        x = FE
    elif tower == "JC":
        x = JC
    elif tower == "Iv":
        x = Iv
    elif tower == "CB":
        x = CB
    elif tower == "Y":
        x = Y
    else:
        print("Invalid input")
        continue

    y = int(input("Please input number of towers: "))
    z = int(input("Please input CPS: "))
    increase = 1.15

    result = z / (x * increase ** y)
    print("The result is:", result)

    confirm = input("Would you like to confirm? (y/n): ")
    if confirm == "y":
        print("Confirmed. Last result:", result)
        last_result = result
    elif confirm == "n":
        continue
    else:
        print("Invalid input. Please try again.")
