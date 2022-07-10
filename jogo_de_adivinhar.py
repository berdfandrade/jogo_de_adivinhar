from random import randint as ri


def inp(text):
    return int(input(text))

n = ri(1, 100)

advinhe = inp("Adivinhe o número de 1 a 100:  ")
while True:
    if advinhe < n:
        print("\n Muito baixo!\n")
        advinhe = inp("Tente de novo!: ")
        print("=================")
    
    elif advinhe > n:
        print("\n Muito alto\n")
        advinhe = inp("Tente de novo!:  ")
        print("=================")
        
    else:
        print("\n\n Você acertou!")
        print(("\n\n Até mais!\n\n"))
        break

