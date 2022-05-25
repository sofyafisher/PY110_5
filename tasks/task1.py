def conventer(list_):
    binary = "".join([str(x) for x in list_])
    decimal = int(binary, 2)
    return decimal
