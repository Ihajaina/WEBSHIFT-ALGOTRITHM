#exercice 2
#exercice 2
from itertools import product

dictionnaire = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.',  'H': '....', 'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',  'T': '-',    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}
def codage(compter):
    return ''.join(dictionnaire.get(i.upper()) for i in compter.split())

def longueur(morse):
    possible_messages = ['bonjour', 'coucou', 'aurevoir', 'byebye']
    point = morse.count('.')
    trait = morse.count('-')
    for combo in product('.-', repeat=point+trait):
        possible_morse = ''.join(combo).replace('.', '*'*point).replace('-', '*'*trait)
        if morse == possible_morse:
            message = codage(possible_morse)
            if message not in possible_messages:
                possible_messages.append(message)
    return len(possible_messages)
type_code = '-...----..------..-.-.'
num_messages = longueur(type_code)
print(f"Il y a {num_messages} messages différents qui produisent le code Morse '{type_code}'")


