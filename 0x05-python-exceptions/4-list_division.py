def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                value1 = my_list_1[i]
                value2 = my_list_2[i]
                try:
                    result = float(value1) / float(value2)
                    result_list.append(result)
                except ZeroDivisionError:
                    result_list.append(0)
                    print("division by 0")
                except (ValueError, TypeError):
                    result_list.append(0)
                    print("wrong type")
            except IndexError:
                print("out of range")
                break
    except TypeError:
        pass
    finally:
        return result_list
