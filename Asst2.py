from Node import Node
from Stack import Stack
from Queue import Queue
from BinaryTree import BinaryTree

def evaluate_expression(infix):
    infix_list = infix.split()
    s = Stack()
    postfix = []
    for i in infix_list:
        if i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix.append(s.pop())
            s.pop()
        elif i in '<>':
            try:
                while s.peek() != '(':
                    postfix.append(s.pop())
            except IndexError:
                pass
            s.push(i)
        elif i in '+-':
            try:
                while s.peek() != '(' and s.peek() not in '<>':
                    postfix.append(s.pop())
            except IndexError:
                pass
            s.push(i)                        
        elif i in '*/':
            try:
                while s.peek() != '(' and s.peek() not in '<>+-':
                    postfix.append(s.pop())
            except IndexError:
                pass
            s.push(i)
        elif i == '^':
            try:
                while s.peek() == '^':
                    postfix.append(s.pop())
            except IndexError:
                pass
            s.push(i)
        else:
            postfix.append(i)

    while not s.is_empty():
        postfix.append(s.pop())

    print(postfix)
    return evaluate_postfix(postfix)

def compute(num1, num2, operator):
    if operator == '<':
        if num1 < num2:
            return num1
        else:
            return num2
    elif operator == '>':
        if num1 > num2:
            return num1
        else:
            return num2    
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 // num2
    else:
        return num1 ** num2

def evaluate_postfix(expression):
    s = Stack()
    result = ''
    operators = '<>+-*/^'
    for char in expression:
        if char in operators:
            num2 = int(s.pop())
            num1 = int(s.pop())
            s.push(compute(num1, num2, char))
        else:
            s.push(char)            
    return s.pop()            

def generate_chain(start, n):
    head = Node(start)
    current = head
    for i in range(n -1):
        num_str = str(current.get_data())
        tot = 0
        for num in num_str:
            tot += int(num)            
        new_node = Node(current.get_data() + tot)
        current.set_next(new_node)
        current = new_node        
    return head

def move_node_to_end(head, value):
    current = head
    prev = None
    item = None
    while current.get_next() != None:
        if current.get_data() == value:
            prev.set_next(current.get_next())
            item = current
        prev = current
        current = current.get_next()
    if item != None:
        current.set_next(item)
        item.set_next(None)

def create_tree_from_nested_list(node_list):
    if not node_list:
        return
    h = node_list[0]
    l = node_list[1]
    r = node_list[2]
    tree = BinaryTree(h)
    tree.set_left(create_tree_from_nested_list(l))
    tree.set_right(create_tree_from_nested_list(r))
    return tree    

def create_tree_from_flat_list(node_list):
        return create_tree_from_flat_list_with_index(node_list, i=1)

def create_tree_from_flat_list_with_index(node_list, i):
        if not node_list[i]:
            return
        t = BinaryTree(node_list[i])
        try:
            t.set_left(create_tree_from_flat_list_with_index(node_list, i *2))
        except IndexError:
            pass
        try:
            t.set_right(create_tree_from_flat_list_with_index(node_list, i *2 +1))
        except IndexError:
            pass
        return t

def breadth_first(t):
    breadth_first_list = []
    q = Queue()
    q.enqueue(t)
    while not q.is_empty():
        l = q.peek().get_left()
        if l != None:
            q.enqueue(l)
        r = q.peek().get_right()
        if r != None:
            q.enqueue(r)
        breadth_first_list.append(q.dequeue().get_data())
        
    return breadth_first_list
        

def mirror(t):
    if not t:
        return
    temp = t.get_left()
    t.set_left(t.get_right())
    t.set_right(temp)
    mirror(t.get_left())
    mirror(t.get_right())
    

def hashing(keys, table_size, probe_type, q):
    hash_list = [None for i in range(table_size)]

    if probe_type == 'linear':
        for k in keys:
            hash_key = k % table_size
            while hash_list[hash_key] != None:
                hash_key += 1
                hash_key %= table_size
            hash_list[hash_key] = k

    elif probe_type == 'quadratic':
        for k in keys:
            hash_key = k % table_size
            index = 1
            while hash_list[hash_key] != None:
                hash_key += index **2 
                index += 1
                hash_key %= table_size
            hash_list[hash_key] = k

    elif probe_type == 'double':        
        for k in keys:
            hash_key = k % table_size
            hash_step = q - (k % q)
            while hash_list[hash_key] != None:
                hash_key += hash_step
                hash_key %= table_size
            hash_list[hash_key] = k

    return hash_list

def create_binary_search_tree(node_list):
    pass

def min_waste(space_left, items):
    pass

