from DataStructures.List import list_node as ln

def new_list(): 
    newlist = {
        "first": None, 
        "last": None, 
        "size": 0
    }
    return newlist

def get_element(my_list, pos): 
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos: 
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function): 
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None: 
        if cmp_function(element, temp["info"]) == 0: 
            is_in_array = True
        else: 
            temp = temp["next"]
            count += 1
            
    if not is_in_array: 
        count = -1
    return count

def add_first(mylist, element):
    
    new_node = ln.new_single_node(element)
    
    if mylist['size'] == 0:
        mylist['first'] = new_node
        mylist['last'] = new_node
        
        mylist['size'] = 1
        return None
    
    else:
        first_node = mylist['first']
        
        new_node['next'] = first_node
        mylist['first'] = new_node
    
        mylist['size'] += 1
        return None

def add_last(my_list, element):
    
    new_node = ln.new_single_node(element)
    
    if my_list['size'] == 0:
        my_list['first'] = new_node
        my_list['last'] = new_node
        
        my_list['size'] = 1
        return None
    
    else:
        last_node = my_list['last']
    
        last_node['next'] = new_node
        my_list['last'] = new_node
    
        my_list['size'] += 1
        return None
    

def size(my_list):
    size = my_list['size']
    
    return size

def first_element(my_list):
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range')
    
    else:
        first = my_list['first']['info']
        return first
    
def delete_element(my_list, pos): 
    node = my_list['first']
    
    if pos < 0 or pos >= size(my_list): 
        raise Exception('IndexError: list index out of range')
    
    elif pos == 0: 
        my_list['first'] = my_list['first']['next']
    
    else: 
        prev = None
        searchpos = 0
        while searchpos < pos: 
            prev = node 
            node = node["next"]
            searchpos += 1
        prev["next"] = node["next"]
        if prev["next"] == None: 
            my_list['last'] = prev
    my_list['size'] -= 1
    return my_list

def remove_first(my_list): 
    if my_list['size'] == 0: 
        raise Exception('IndexError: list index out of range')
    
    else: 
        first = my_list['first']['info']
        delete_element(my_list, 0)
        return first


def remove_last(my_list): 
    if my_list['size'] == 0: 
        raise Exception('IndexError: list index out of range')
    
    else: 
        last = my_list['last']['info']
        delete_element(my_list, my_list['size'] - 1)
        return last
 
def insert_element(my_list, element, pos): 
    new_node = ln.new_single_node(element)
    
    if pos < 0 or pos > size(my_list): 
        raise Exception('IndexError: list index out of range')
    
    elif pos == 0: 
        add_first(my_list, element)
    
    elif pos == size(my_list):
        add_last(my_list, element)
    
    else: 
        searchpos = 0
        prev = None
        node = my_list['first']
        
        while searchpos < pos: 
            prev = node 
            node = node["next"]
            searchpos += 1
        prev["next"] = new_node
        new_node["next"] = node
        my_list['size'] += 1
        
    return my_list

def exchange(my_list, pos_1, pos_2): 
    if pos_1 < 0 or pos_1 > size(my_list) or pos_2 < 0 or pos_2 > size(my_list): 
        raise Exception('IndexError: list index out of range')
    
    elif pos_1 == pos_2: 
        return my_list
    
    else: 
        search_pos1 = 0 
        prev1 = None
        node1 = my_list['first']
        while search_pos1 < pos_1: 
            prev1 = node1
            node1 = node1["next"]
            search_pos1 += 1 
            
        search_pos2 = 0 
        prev2 = None
        node2 = my_list['first']
        while search_pos2 < pos_2: 
            prev2 = node2
            node2 = node2["next"]
            search_pos2 += 1
        
        temp1 = node1["next"]
        temp2 = node2["next"]
        prev1["next"] = node2  
        node2["next"] = temp1
        prev2["next"] = node1
        node1["next"] = temp2
    return my_list
        
    first = my_list['first']['info']
    return first
    
def is_empty(my_list):
    return my_list['size'] == 0

def last_element(my_list):
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range')
    
    last = my_list['last']['info']
    return last

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError('list index out of range')
    
    i = 0
    current = my_list['first']
    while i != pos:
        current = current['next']
        i += 1
    
    current['info'] = new_info
    
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError('list index out of range')
    
    if num_elements < 0:
        raise IndexError('list index out of range')
    
    if pos_i + num_elements > my_list['size']:
        raise IndexError('list index out of range')
    
    i = 0
    current = my_list['first']
    while i != pos_i:
        current = current['next']
        i += 1
    
    nlist = new_list()
    
    j = 0
    while j < num_elements:
        add_last(nlist, current['info'])
        current = current['next']
        j += 1
    
    return nlist