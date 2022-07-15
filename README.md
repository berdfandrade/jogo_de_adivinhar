# Jogo de advinhar 
![GitHub top language](https://img.shields.io/github/languages/top/berdfandrade1/jogo_de_adivinhar?color=f&label=Python&logo=python&logoColor=fff)

Jogo simples de adivinhar um número de 1 a 100, escrito em Python

A parte de "randomização" do jogo, foi feita com a biblioteca [random](https://docs.python.org/pt-br/3.8/library/random.html)
```
from random import randint as ri
```
Após isso, eu usei o método [randit](https://www.w3schools.com/python/ref_random_randint.asp) para gerar um número de 1 a 100.

O número de 1 a 100, é a variável `n`.
```
n = ri(1, 100)
```
Agora, algum número aleatório de `1 a 100` está armazenado na memória do código. E o que precisamos fazer agora é criar um `input`, para que o usuário possa tentar advinhar o número. O input contém a string `"Adivinhe o número de 1 a 100:  "` > Desta forma o usuário vê no console essa string.


```
$ Adivinhe o número de 1 a 100:
```


A partir do `while loop` com um `if statement` dentro, podemos verificar se o input do usuário está próximo do número armazenado no código. Porém, o interessante, é que também não sabemos qual número que é. 




```
while True:
    if advinhe < n:
        print("\n Muito baixo!\n")
        advinhe = inp("Tente de novo!: ")
        print("=================") 
```
Também printamos o input `"Tente de novo:"` para o jogador continuar com o loop, e com o jogo. 



E por fim, temos o resto do `if statement`: 


```
    elif advinhe > n:
        print("\n Muito alto\n")
        advinhe = inp("Tente de novo!:  ")
        print("=================")

    else:
        print("\n\n Você acertou!")
        print(("\n\n Até mais!\n\n"))
        break
``` 

Quando o jogador acerta o número, usamos o `else` do `if statement` para verficar que o número colocado pelo usuário, não é maior, nem menor que o número gerado. Assim, terminamos printamos um `Você acertou!`, para mostrar que o jogador ganhou o jogo. Logo em seguida, saímos do loop com um `break`.
