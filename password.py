from random import choice






if __name__  == '__main__':
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '@', '/',
             ' ', '-', '_', '&', '*', '$', '%', '!', '.', '?', '&', "'",
             '"', ')', '=', '#', '{', '}', '(', '[', ']']
    alphamin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphamax = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphanbre = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    ch =input("1 : all characters , 2: lowercase letters : , 3: uppercase , 4: numbers :")

    if ch == '1':
        fitchingtab = alpha
    elif ch == '2':
        fitchingtab = alphamin
    elif ch == '3':
        fitchingtab = alphamax
    elif ch == '4':
        fitchingtab =alphanbre
    print(len(fitchingtab))




    l=8
    fileName = "fichier"
    for harf in fitchingtab:
        for harf2 in fitchingtab:
            for harf3 in fitchingtab:
                for harf4 in fitchingtab:
                    for harf5 in fitchingtab:
                        for harf6 in fitchingtab:
                            for harf7 in fitchingtab:
                                for harf8 in fitchingtab:
                                    fileContent = harf + harf2 + harf3 + harf4 + harf5 + harf6 + harf7 + harf8
                                    f = open(fileName + ".txt", "a+")
                                    f.write(fileContent + "\n")
    f.close()
    print("done go check it ")