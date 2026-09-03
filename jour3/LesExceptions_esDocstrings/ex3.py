class NumberError(Exception):
    pass
def calculer_carre(nombre):
    if type(nombre) is not int or float:
        NumberError('Le paramètre doit être un nombre')
    if nombre<0:
        ValueError('Le nombre ne peut pas être négatif')
    return nombre**2

print(calculer_carre(2))