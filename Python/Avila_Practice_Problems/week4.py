a = list([1,2,3])
print(a)


# wont work a = list(1,2,3)
#print(a)


a = list[1,2,3]
print(a)

# Create Container#####################################

def create_container(container_type):
    if container_type == 'list':
        return []

    elif container_type == 'dict':
        return {}

    elif container_type == 'set':
        return set()

    elif container_type == 'tuple':
        return ()


# Access Elements ##############################################
def access_item(item, container):
    if  isinstance(container, list):
         return container[item]
    
    elif isinstance(container, dict):
        return container[item]
    
    elif isinstance(container, tuple):
        return container[item]
    
    elif isinstance(container, set):
            return item in container


assert access_item(2, [1, 2, 3, 4]) == 3
container = {1: 'a', 3: 'c', 4: 'd'}
assert access_item(3, container) == 'c'
assert access_item(2, {1, 2, 3, 4}) == True
assert access_item(5, {1, 2, 3, 4}) == False
assert access_item(2, (1, 2, 3, 4)) ==3



### Step 3: Implementing the add_item function

def add_item(item, container, position=None):
    if isinstance(container,list):
        if position is not None:
            container.insert(position, item)
        else:
            container.append(item) 

        return container

    elif isinstance(container,dict):
        if isinstance(item, tuple) and len(item) ==2:
            container[item[0]] = item[1]
        else:
            container[item] = None

        return container

    elif isinstance(container,tuple):
        if position is None: 
            container = container +(item,)
        else:
            #[:position]   = BEFORE the position
            #[position:]   = AT the position and everything after
            container = container[:position] + (item,) + container[position:]
        return container

    elif isinstance(container,set):
        container.add(item)

        return container

assert add_item(5, [1, 2, 3, 4]) == [1, 2, 3, 4, 5]
assert add_item('c', ['a', 'b', 'd', 'e'], 2) == ['a', 'b', 'c', 'd', 'e']
container = {1: 'a', 3: 'c', 4: 'd'}
assert (add_item(2, container) == {1: 'a', 2: None, 3: 'c', 4: 'd'})
container = {1: 'a', 3: 'c', 4: 'd'}
assert (add_item((2, 'b'), container) == {1: 'a', 2: 'b', 3: 'c', 4: 'd'})
assert add_item(2, {1, 4}) == {1, 4, 2}
assert add_item(5, (1, 2, 3, 4)) == (1, 2, 3, 4, 5)
assert add_item('c', ('a', 'b', 'd', 'e'), 2) == ('a', 'b', 'c', 'd', 'e')


#Remove Elements (Task)
# Step 4: Implementing the remove_item function

def remove_item(item, container, multi=True):

    if isinstance(container, list):
        
        if multi==True:

            for x in container[:]:
                if x == item:
                    container.remove(item)
        else:
            container.remove(item)

        return container

            

    elif isinstance(container, dict):
        
        del container[item]

        return container


        

    elif isinstance(container, set):

        container.discard(item)

        return container
        

    elif isinstance(container, tuple):
        index = container.index(item)

        if multi == False:
            container = container[:index] + container[index +1:]

        elif multi == True:
                container = tuple(x for x in container if x != item)

        return container    
        
assert remove_item(1, [1, 2, 3, 4, 1]) == [2, 3, 4]
assert remove_item(1, [1, 2, 3, 4, 1], False) == [2, 3, 4, 1]
container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
assert remove_item(2, container) == {1: 'a', 3: 'c', 4: 'd'}
assert remove_item(3, {1, 2, 3, 4}) == {1, 2, 4}
assert remove_item(1, (1, 2, 3, 4, 1)) == (2, 3, 4)
assert remove_item(1, (1, 2, 3, 4, 1), False) == (2, 3, 4, 1)


def update_item( orig_item, new_item, container, multi=True):
    if isinstance(container, list):
        if multi==True:
            # enumerate gives you the index and the value back 
            for index, x in enumerate(container):
                if x == orig_item:
                    container[index] = new_item 
                    
    
        else:
            for index, x in enumerate(container):
                            if x == orig_item:
                                container[index] = new_item  
                                break

        return container

    elif isinstance(container, set):
        container.remove(orig_item)
        container.add(new_item)

        return container 
        

    elif isinstance(container, tuple):
        place_holder_list = list(container)
        if multi==True:
            for index, x in enumerate(place_holder_list):
                if x == orig_item:
                    place_holder_list[index] = new_item
                    
                    
        else:     
            for index, x in enumerate(place_holder_list):
                if x == orig_item:
                    place_holder_list[index] = new_item
                    break

        container = tuple(place_holder_list)            
        return container

    elif isinstance(container, dict):

        if isinstance(new_item, tuple):
            container.pop(orig_item)
            container[new_item[0]] = new_item[1]

        else:
            container[orig_item] = new_item

        return container
        

assert update_item(1, 8, [1, 2, 3, 4, 1]) == [8, 2, 3, 4, 8]
assert update_item(1, 8, [1, 2, 3, 4, 1], False) == [8, 2, 3, 4, 1]
assert update_item(2, 8, {1, 2, 3, 4}) == {1, 8, 3, 4}
assert update_item(2, 8, {1, 2, 3, 4}, multi=False) == {1, 8, 3, 4}
container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
assert update_item(1, 'h', container) == {1: 'h', 2: 'b', 3: 'c', 4: 'd'}
container = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
assert update_item(1, (5, 'h'), container) == {5: 'h', 2: 'b', 3: 'c', 4: 'd'}
assert update_item(1, 8, (1, 2, 3, 4, 1)) == (8, 2, 3, 4, 8)


def convert_container(container, container_type):
    
    if container_type == 'list':
        if isinstance(container, dict):
             return list(container.items())
        else:
            return list(container)

  
    elif container_type == 'set':
        if isinstance(container, dict):
            return set(container.items())
        else:
            return set(container)

    elif container_type == 'tuple':
        if isinstance(container, dict):
            return tuple(container.items())
        else:
            return tuple(container)

        
    
    elif container_type == 'dict':
        new_container = {}
        for item in container:
            if isinstance(item, tuple) and len(item) == 2:
                new_container[item[0]] = item[1]

            else:
                new_container[item] = None
                

        return new_container

assert convert_container([1, 2, 3, 4], 'dict') ==\
        {1: None, 2: None, 3: None, 4: None}
assert convert_container([1, (2, 'a'), 3, (4, 'b')], 'dict') ==\
        {1: None, 2: 'a', 3: None, 4: 'b'}
assert convert_container([1, 2, 3, 4], 'set') == {1, 2, 3, 4}
assert convert_container([1, 2, 3, 4], 'tuple') ==\
        (1, 2, 3, 4)

orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
new_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
assert sorted(convert_container(orig_dict, 'list')) == new_list

orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
new_set = {(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')}
assert convert_container(orig_dict, 'set') == new_set

orig_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
ref_tuple = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))
new_tuple = convert_container(orig_dict, 'tuple')
assert type(new_tuple) is tuple
assert tuple(sorted(new_tuple)) == ref_tuple

assert sorted(convert_container({1, 2, 3, 4}, 'list')) == [1, 2, 3, 4]

assert convert_container({1, 2, 3, 4}, 'dict') ==\
        {1: None, 2: None, 3: None, 4: None}

assert convert_container({1, (2, 'a'), 3, (4, 'b')}, 'dict') ==\
        {1: None, 2: 'a', 3: None, 4: 'b'}

new_tuple = convert_container({1, 2, 3, 4}, 'tuple')
assert type(new_tuple) is tuple
assert tuple(sorted(new_tuple)) ==\
    (1, 2, 3, 4)

assert convert_container((1, 2, 3, 4), 'list') ==\
        [1, 2, 3, 4]
assert convert_container((1, 2, 3, 4), 'dict') ==\
        {1: None, 2: None, 3: None, 4: None}
assert convert_container((1, (2, 'a'), 3, (4, 'b')), 'dict') ==\
        {1: None, 2: 'a', 3: None, 4: 'b'}
assert convert_container((1, 2, 3, 4), 'set') == {1, 2, 3, 4}