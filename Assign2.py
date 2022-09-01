from code_check import *

def basic(code):
    '''
    print("ISBN passing in is:", code)
    for i in code:
        a = int(i)

    return True
    :param code:
    :return:
    '''



def main():
    #print("hello world")
    #a = basic("24528348")
    #a = basic_code("434134")
    #b = universal_product_code("80663341344")
    #b = positional_code("24528349")
    #print(a)
    #print(b)
    run = True
    basic_list = []
    position_list = []
    upc_list = []
    none_list = []
    while run:
        none_check = False
        counter = 0
        barcode = input("Please enter code (digits only)(enter 0 to quit) ")
        if barcode == '0':
            break
        if int(barcode) <= 0:
            run = False

        if basic_code(barcode):
            counter += 1
            basic_list.append(barcode)
            print("--code", barcode,"valid Basic code")

        if positional_code(barcode):
            counter += 1
            position_list.append(barcode)
            print("--code", barcode, "valid Position code")

        if universal_product_code(barcode):
            counter += 1
            print("--code", barcode, "valid UPC code")
            upc_list.append(barcode)
        if counter == 0:
            print("--code", barcode, "not Basic, Position or UPC code.")
            none_list.append(barcode)
    if len(basic_list) == 0:
        basic_list.append('None')
    if len(position_list) == 0:
        position_list.append('None')
    if len(upc_list) == 0:
        upc_list.append('None')
    if len(none_list) == 0:
        none_list.append('None')
    print("\nSummary")
    print("Basic :",", ".join(basic_list))
    print("Position :",", ".join(position_list))
    print("UPC :",", ".join(upc_list))
    print("None :", ", ".join(none_list))
    quit()



main()
