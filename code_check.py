

def basic_code(UPC):
    uppp = int(UPC)
    digit = 0
    UPC1 = UPC[:-1]
    for i in UPC1:
        digit += int(i)
    modulo = digit % 10
    last_char = int(UPC[-1])
    if modulo == last_char:
        return True
    else:
        return False

def positional_code(UPC):
    digit = 0
    index = 0
    UPC1 = UPC[:-1]
    for idx, i in enumerate(UPC1):
        index = index + 1
        #print('i', i, 'index', index)
        digit += int(i) * index
        #print(digit)
    modulo = digit % 10
    last_char = int(UPC[-1])
    if modulo == last_char:
        return True
    else:
        return False
def universal_product_code(UPC):
    digit = 0
    UPC1 = UPC[:-1]
    for idx, i in enumerate(UPC1):
        if idx % 2 == 1:

            digit += int(i)

        elif idx % 2 == 0:

            digit += int(i) * 3

    modulo = digit % 10
    if modulo == 0:
        checkDigit = 0
    elif modulo < 10:
        checkDigit = 10 - modulo
    last_char = int(UPC[-1])
    if(checkDigit == last_char):
        return True
    else:
        return False


    '''    
    for i, char in enumerate(UPC):
        for j in UPC:
            
        if int(i) % 2 == 0:
            
            digit += int(i)
        elif int(i) % 2 == 1:
            print("odd",i)
            digit += int(i)*3
    '''


    print(digit)
    return True
