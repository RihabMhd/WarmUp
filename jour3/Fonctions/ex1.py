from ..LesExceptions_esDocstrings.ex3 import NumberError

def compute_list_sum(list):
    for l in list:
        if type(l) is not int:
            NumberError('Le paramètre doit être un nombre')
    return sum(list)

print(compute_list_sum([1,2,5,8]))