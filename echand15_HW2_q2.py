import numpy as np

# process to encrypt
def encrypt():

    pt = input("Plain Text: ")

    row = int(input("Matrix row size: "))
    col = int(input("Matrix column size: "))
    rowArr = input("Row Permutation Order:")
    colArr = input("Column Permutation Order:")
    rowPerm = list(map(int, rowArr.split(", ")))
    colPerm = list(map(int, colArr.split(", ")))

# to encrypt into array
    array = np.zeros(shape=(row, col), dtype=object)
    j = 0
    y = 0
    while y < row:
        i = 0
        x = 0
        while col > i:
            if (len(pt) > j):
                if (pt[j] == " "):
                    array[rowPerm[y] - 1][colPerm[x] - 1] = "x"
                else:
                    array[rowPerm[y] - 1][colPerm[x] - 1] = pt[j]
            else:
                array[rowPerm[y] - 1][colPerm[x] - 1] = "x"
            x += 1
            i += 1
            j += 1
        y += 1

# print out encrypted text
    x = 0
    y = 0
    encryptedPrint = ""
    while y < row:
        while x < col:
            encryptedPrint += array[y][x]
            x += 1
        x = 0
        y += 1

    print(encryptedPrint)

# process to unencrypt
def unEncrypt():

    et = input("Encrypted Text: ")

    row = int(input("Matrix row size: "))
    col = int(input("Matrix column size: "))
    rowArr = input("Row Permutation Order:")
    colArr = input("Column Permutation Order:")
    rowPerm = list(map(int, rowArr.split(", ")))
    colPerm = list(map(int, colArr.split(", ")))

# build array to read
    encryptedArray = np.zeros(shape=(row, col), dtype=object)

    y = 0
    i = 0

    while y < row:
        x = 0
        while x < col:
            encryptedArray[y][x] = et[i]
            i += 1
            x += 1
        y += 1

#unencrypt

    y = 0
    unEncryptedPrint =  ""

    while y < row:
        i = 0
        while i < col:
            if (encryptedArray[(rowPerm[y])-1][(colPerm[i])-1] != "x"):
                unEncryptedPrint += encryptedArray[(rowPerm[y])-1][(colPerm[i])-1]
            else:
                unEncryptedPrint += " "
            i += 1
        y +=1
    print(unEncryptedPrint)


run = True
while run == True:
    x = input("Select Mode \n '1' for Encrypt \n '2' for Decrypt \n Other Key will exit")
    if x == '1':
        encrypt()
    elif x == '2':
        unEncrypt()
    else:
        exit()