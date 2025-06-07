import re
#Reemplazar todas las apariciones de una palabra en una cadena
text = "Python es divertido. Amo programar en Python."
word_pattern = r'Python'
replaced_text = re.sub(word_pattern, 'Java', text)
print(replaced_text)  # 'Java es divertido. Amo programar en Java.'
