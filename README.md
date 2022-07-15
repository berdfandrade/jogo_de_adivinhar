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
Agora, algum número aleatório de `1 a 100` está armazenado na memória do código. E o que precisamos fazer agora é criar um `input`, para que o usuário p
```
