def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            
            if not isinstance(val_1, (int, float)) or not isinstance(val_2, (int, float)):
                raise TypeError("wrong type")
            
            if val_2 == 0:
                raise ZeroDivisionError("division by 0")
            
            result.append(val_1 / val_2)
        
        except IndexError as e:
            print("Error:", e)
            return
        
        except TypeError:
            print("Error: wrong type")
            result.append(0)
        
        except ZeroDivisionError:
            print("Error: division by 0")
            result.append(0)
        
        finally:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("Error: out of range")
                return
    
    return result
