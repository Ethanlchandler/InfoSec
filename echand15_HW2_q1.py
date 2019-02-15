#definitions

abcs ='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

#Make Pass phrase long enough
def passEqualPlain(pp, pt):

    while len(pp) < len(pt):
        pp =  pp + pp
    return pp

#Cipher Def
def cipher(pp, pt):
    #get pp to equal pt for ciphering
    pp = passEqualPlain(pp,pt)
    # declare variable
    ppi = 0
    i = 0
    ciphered = ""
    #begin cipher
    while i <= len(pt) -1:
        if pt[i] != " ":
            temp = abcs.index(pt[i]) + abcs.index(pp[ppi])
            ciphered += abcs[temp]
            ppi += 1
        elif pt[i] == " ":
            ciphered += " "
        else:
            print("Error Encoutnered")
        i += 1
    print("Encoded Text: " + ciphered )

#Decipher Def
def decipher(pp, et):
    #get pp to equal pt for ciphering
    pp = passEqualPlain(pp,et)
    # declare variable
    ppi = 0
    i = 0
    deciphered = ""
    #begin cipher
    while i <= len(et) -1:
        if et[i] != " ":
            if abcs.index(et[i]) >= abcs.index(pp[ppi]):
                temp = abcs.index(et[i]) - abcs.index(pp[ppi])
            else:
                temp = (abcs.index(et[i])+26) - abcs.index(pp[ppi])
            deciphered += abcs[temp]
            ppi += 1
        elif et[i] == " ":
            deciphered += " "
        else:
            print("Error Encoutered")
        i += 1
    print("Decoded Plain Text: " + deciphered)




#MAIN PROGRAM
# Cipher or Decipher Mode
run = 1
while run == 1:
    mode = input("Enter '1' or '2': \n 1. Ciphering  \n 2.Deciphering \n Quit with any other input. ")
    if mode == '1':
        plainText = input("Ciphering Mode\n" "Enter Plain Text to be Encoded:")
        passPhrase = input("Enter Pass Phrase (no spaces allowed):")
        cipher(passPhrase, plainText)

    elif mode == '2':
        encText = input("Deciphering Mode\n""Enter Encoded Text to be Decoded:")
        passPhrase = input("Enter Pass Phrase(no spaces allowed):")
        decipher(passPhrase, encText)
    else:
        break
