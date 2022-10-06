from random import randint
def input_dat(name):
    x = int(input(f"{name}, Введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, Введите корректное количество конфет от 1 до 28: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ход {name}, он взял {k}, теперь у него {counter} конфет. Осталось на столе {value} конфет.")


def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

igrok1 = input("Введите имя первого игрока: ")
igrok2 = "Bot"
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2)
if flag:
    print(f"Первый ход по жеребревки {igrok1}")
else:
    print(f"Первый ход по жеребревки {igrok2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(igrok1)
        counter1 += k
        value -= k
        flag = False
        p_print(igrok1, k, counter1, value)
    else:
        k = randint(1,29)
        counter2 += k
        value -= k
        flag = True
        p_print(igrok2, k, counter2, value)

if flag:
    print(f"Выиграл {igrok1}")
else:
    print(f"Выиграл {igrok2}")
