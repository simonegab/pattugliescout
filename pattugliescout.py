import random

def assign_pattuglie(num_pers, num_patt, list_pers, list_patt_names):
    # Mischiare casualmente la lista delle persone
    random.shuffle(list_pers)

    # Distribuire equamente le persone tra le pattuglie
    pers_per_patt = num_pers // num_patt
    remainder = num_pers % num_patt

    start = 0
    list_patt = []

    for ii in range(num_patt):
        end = start + pers_per_patt + (1 if ii < remainder else 0)
        pattuglia = list_pers[start:end]
        list_patt.append((list_patt_names[ii], pattuglia))
        start = end

    return list_patt

def rotate_list(lst, shift):
    return lst[shift:] + lst[:shift]

# Numero e Nomi di Persone
num_pers = int(input("Inserire il numero di persone: "))
list_pers = [None] * num_pers
for i in range(num_pers):
    list_pers[i] = input("Inserire nome persona: ")

# Numero e Nomi delle Pattuglie
num_patt = int(input("Inserire il numero di pattuglie da generare: "))
list_patt_names = [None] * num_patt
for ii in range(num_patt):
    list_patt_names[ii] = input("Inserire nome pattuglia: ")

# Numero di ripetizioni desiderate
num_ripetizioni = int(input("Inserire il numero di ripetizioni desiderate: "))

# Lista per tracciare le assegnazioni di ogni ripetizione
all_ripetizioni = []

# Generare le ripetizioni con assegnazioni diverse
for _ in range(num_ripetizioni):
    list_patt = assign_pattuglie(num_pers, num_patt, list_pers, list_patt_names)
    all_ripetizioni.append(list_patt)
    
    # Ruota la lista delle persone in modo che ognuna finisca in una diversa pattuglia
    list_pers = rotate_list(list_pers, num_pers // num_patt)

print()

# Stampare le distribuzioni di tutte le ripetizioni
for i, ripetizione in enumerate(all_ripetizioni):
    print(f"Ripetizione {i + 1}:")
    for pattuglia_name, pattuglia in ripetizione:
        print(f"{pattuglia_name}: {', '.join(pattuglia)}")
    print()