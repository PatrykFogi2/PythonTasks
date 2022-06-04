import random

def warm_cold():
    random_number = random.randint(1,51)
    guess_number = 0
    count = 0
    print('zgadnij liczbe od 1 do 50')
    while (random_number != guess_number):
        if guess_number == -1:
            break
        count += 1
        guess_number = int(input('wpisz liczbe'))
        if guess_number > random_number:
            print('Podana liczba jest za duza')
        if guess_number < random_number and guess_number >0:
            print('Podana liczba jest za mala')

    else:
        print(f'gratulacje, liczba sie zgadza, potrzebowales {count} prob')

warm_cold()