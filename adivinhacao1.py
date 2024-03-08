import random
max_rand = 10

print(" BEM VINDO AO JOGO DA ADIVINHAÇÃO ")

dificuldade = int(input("Digite a dificuldade:\n 1 - Fácil\n 2 - Médio\n 3 - Difícil  "))

if dificuldade == 1 :
    limite_tentativas = 10
elif dificuldade == 2 :
    limite_tentativas = 5
elif dificuldade == 3 :
    limite_tentativas = 3

else :
    print("Dificuldade inválida!")

sorteio = random.randint(0, max_rand)

tentativa = 1

print("Tente adivinhar o número de 0 a 10, em {} tentativas!".format(limite_tentativas))
while (tentativa <= limite_tentativas) :
    chute = int(input("Digite o valor do seu chute: \n"))

    acertou = chute == sorteio
    maior   = chute  > sorteio
    menor   = chute  < sorteio

    if (acertou):
        print("Parabéns, você acertou!")
        break
    elif (maior):
        print("O número que você digitou é maior")
    elif (menor):
        print("O número que você digitou é menor")
    tentativa = tentativa + 1


print(" O número sorteado era: ", sorteio, "")

print(" FIM DO JOGO ")