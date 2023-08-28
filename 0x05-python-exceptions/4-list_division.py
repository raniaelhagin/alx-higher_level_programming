#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ArithmeticError:
            result = 0
            print("division by zero")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("outof range")
        finally:
            new_list.append(result)
    return new_list
