from DataStructures.List import single_linked_list as lt

def new_stack(): 
    return lt.new_list()

def push(my_stack, element): 
    lt.add_last(my_stack, element)
    return my_stack

def pop(my_stack): 
    if is_empty(my_stack): 
        raise Exception('EmptyStructureError: stack is empty')
    else: 
        return lt.remove_last(my_stack)

def is_empty(my_stack):
    return lt.is_empty(my_stack)

def top(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    
    else:
        t = lt.last_element(my_stack)
        return t

def size(my_stack):
    sz = lt.size(my_stack)
    return sz
