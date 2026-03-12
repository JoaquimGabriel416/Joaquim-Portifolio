def menu():
    print('''--MENU--
Seja bem vindo a calculadora Celsius/Farenheit
1. Celsius
2. Farenheit
3. Sair''')

def celsius():
    temp_celsius = float(input("Insira a temperatura em °C: "))
    calculo1 = (temp_celsius*9/5)+32
    print(f'A temperatura {temp_celsius}°C em Farenheit é igual a {calculo1}°F')

def farenheit():
    temp_farenheit = float(input("Insira a temperatura em °F: "))
    calculo2 = (temp_farenheit-32)*5/9
    print(f'A temperatura {temp_farenheit}°F em Celsius é igual a {calculo2}')

while True:
    menu()
    try:
        escolha = int(input('Escolha uma das opções acima: '))
    except ValueError:
        print("Digite apenas números!")
        continue
    if escolha == 1:
        celsius()
    elif escolha == 2:
        farenheit()
    elif escolha == 3:
        break
    else: print('Escolha um numero válido!')