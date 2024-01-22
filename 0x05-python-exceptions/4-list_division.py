#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            if type(element_1) not in (int, float) or type(element_2) not in (int, float):
                raise TypeError("wrong type")

            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            result_list.append(element_1 / element_2)

        except TypeError as e:
            print("Error: {}".format(e))
            result_list.append(0)
        except ZeroDivisionError as e:
            print("Error: {}".format(e))
            result_list.append(0)
        except IndexError:
            print("Error: out of range")
            result_list.append(0)
    return result_list
