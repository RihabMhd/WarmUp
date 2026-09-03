class ZeroException(Exception):
    """Exception levée lorsque le denominateur est zero."""
    pass
class InvalidTypeException(Exception):
    """Exception levée lorsque le type est invalid."""
    pass
def diviser(a, b):
    if b==0:
        raise ZeroDivisionError("le denominateur ne peut pas etre zero")
    if type(b) is not int:
        raise InvalidTypeException("Invalid Type Entree")

    return a//b
print(diviser(10,2))
    