from DataStructures.List import array_list as lt

def new_queue():
    newqueue = lt.new_list()
    return newqueue

def enqueue(my_queue, element):
    lt.add_last(my_queue, element)
    return my_queue

def dequeue(my_queue):
    if my_queue['size'] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    else:
        first = lt.remove_first(my_queue)
        return first

def is_empty(my_queue): 
    return lt.is_empty(my_queue)

def peek(my_queue): 
    if is_empty(my_queue): 
        raise Exception('EmptyStructureError: queue is empty')
    
    else: 
        first = lt.first_element(my_queue)
        return first
    
def size(my_queue): 
    return lt.size(my_queue)