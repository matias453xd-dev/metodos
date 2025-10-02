def parse_int(string):
    # Diccionario de números
    number_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000
    }
    # Por si algun numero tuviera un -
    string = string.replace("-"," ")
    # Dividir la cadena en palabras
    words = string.split()
    result = 0
    current_number = 0

    for word in words:
        if word in number_map:
            value = number_map[word]

            if value == 100:  # Si es "hundred", multiplicamos el número actual
                current_number *= value
            elif value == 1000:  # Si es "thousand", multiplicamos y añadimos al resultado
                current_number *= value
                result += current_number
                current_number = 0
            elif value == 1000000:
                current_number *= value
                result += current_number
                current_number = 0
            else:  # Si es un número normal, lo sumamos al número actual
                current_number += value

    result += current_number  # Añadir cualquier número restante al resultado
    return result


# Pruebas
print(parse_int("seventy four"))               # Salida: 74
print(parse_int("two hundred forty-six"))  # Salida: 123
print(parse_int("two thousand five hundred")) # Salida: 2500
print(parse_int("nineteen"))                  # Salida: 19
print(parse_int("four million"))              # Salida: 4000000