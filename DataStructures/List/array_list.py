def new_list(): 
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0: 
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0: 
                keyexist = True
                break
        if keyexist: 
            return keypos 
    return -1

def add_first(my_list, element):
    list_elements = my_list['elements']
    
    list_elements.insert(0, element)
    my_list['size'] += 1
    
    return None

def add_last(my_list, element):
    list_elements = my_list['elements']
    
    list_elements.append(element)
    my_list['size'] += 1
    
    return None

def size(my_list):
    size = my_list['size']
    
    return size

def first_element(my_list):
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range')
    
    else: 
       first = my_list['elements'][0]
       return first

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        raise IndexError('list index out of range')
        
    else: 
        my_list['elements'].insert(pos, element)
        my_list['size'] += 1
    
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError('list index out of range')
    
    else: 
        my_list['elements'][pos] = new_info
    
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list['size'] or pos2 < 0 or pos2 >= my_list['size']:
        raise IndexError('list index out of range')
    
    else: 
        temp = my_list['elements'][pos1]
        my_list['elements'][pos1] = my_list['elements'][pos2]
        my_list['elements'][pos2] = temp
    
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError('list index out of range')
    
    if num_elements < 0:
        return None
    
    elements = my_list['elements']
    sub_list = elements[pos_i: pos_i+num_elements]
    
    new_list = {
        'elements': sub_list,
        'size': len(sub_list)
    }
    return new_list
    
    

def is_empty(my_list): 
    return size(my_list) == 0

def last_element(my_list): 
    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')
    
    else: 
        last = my_list['elements'][size(my_list) - 1]
        return last
    
def delete_element(my_list, pos): 
    if pos >= 0 and pos < size(my_list): 
        my_list['elements'].pop(pos)
        return my_list
    
    else: 
        raise Exception('IndexError: list index out of range')
    
def remove_first(my_list): 
    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')

    else: 
        first = first_element(my_list)
        my_list['elements'].remove(first)
        my_list['size'] -= 1
        return first

def remove_last(my_list): 
    if is_empty(my_list): 
        raise Exception('IndexError: list index out of range')
    
    else: 
        last = last_element(my_list)
        my_list['elements'].pop(size(my_list) - 1)
        my_list['size'] -= 1
        return last