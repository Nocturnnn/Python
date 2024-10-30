# Solicita ao usuário o número de termos desejado
num_termos = int(input("Digite quantos primeiros termos da sequência de Fibonacci você quer: "))

# Inicializa os primeiros dois termos da sequência
termo1, termo2 = 0, 1
contador = 0

print("Sequência de Fibonacci:")

# Exibe a sequência de Fibonacci até alcançar o número de termos desejado
while contador < num_termos:
    print(termo1, end=" ")
    # Atualiza os valores para os próximos termos da sequência
    proximo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo_termo
    contador += 1