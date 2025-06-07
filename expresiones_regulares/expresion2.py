import re
#Encontrar todas las apariciones de una palabra en una cadena
text = "Python es divertido. Amo programar en Python."
word_pattern = r'\bPython\b'
matches = re.findall(word_pattern, text)
print(matches)  # ['Python', 'Python']
