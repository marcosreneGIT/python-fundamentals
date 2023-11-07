frase = 'Curso em vídeo'
frase_1 = '   Aprenda Python'

print(len(frase))
print(frase.count('o', 0, 6))
print(frase.find('vídeo'))
print('Curso' in frase)
print('')

print(frase.replace('vídeo', 'Python'))
print(frase.upper())
print(frase.lower())
print('')

frase = frase.upper()
print(frase)
frase = frase.capitalize()
print(frase)
print(frase.title())
print('')

print(frase_1)
frase_1 = frase_1.strip()
print(frase_1)
