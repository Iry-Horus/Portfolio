## This is a test program for COMPSCI 105, Summer 2017, Assignment Two.

## It contains all of the example code that appears in the document
## for Assignment Two.  In addition to this example code, you should
## add code of your own to thoroughly test the functions that you have
## defined in the "Asst2.py" source file.  

## You will not submit this file for marking.

## There are the required functions that you must provide in "Asst2.py":
from Asst2 import evaluate_expression
from Asst2 import generate_chain
from Asst2 import move_node_to_end
from Asst2 import create_tree_from_nested_list
from Asst2 import create_tree_from_flat_list
from Asst2 import breadth_first
from Asst2 import mirror
from Asst2 import hashing
from Asst2 import create_binary_search_tree
from Asst2 import min_waste

## You may like to define tests that involve the Node class:
from Node import Node

def print_welcome():
    print('CS105 - Summer School 2017')
    print('Assignment Two')
    print('--------------')
    print('You should develop tests for "Asst2.py" in this source file.')
    print('The "Asst2.py" source file should contain the definitions of')
    print('the required functions for Assignment Two.\n')

def test_Q1():
    expressionA = '2 ^ ( 1 + 3 ^ 2 )'
    expressionB = '( 3 * 5 ) - ( 1 > 2 > 3 < 4 )'
    expressionC = '4 ^ ( 10 < 2 ) / 5 + 100'

    print('Result A =', evaluate_expression(expressionA))
    print('Result B =', evaluate_expression(expressionB))
    print('Result C =', evaluate_expression(expressionC))


def test_Q2():
    my_values = generate_chain(409, 5)

    # Print the chain
    current = my_values
    while current != None:
        print(current.get_data())
        current = current.get_next()

def print_chain_and_ids(chain):
    current = chain
    while current != None:
        print(id(current), current.get_data())
        current = current.get_next()

def test_Q3():	
    a = Node('first')
    b = Node('middle')
    c = Node('last')
    a.set_next(b)
    b.set_next(c)

    print_chain_and_ids(a)
    move_node_to_end(a, 'middle')    

    print_chain_and_ids(a)


def test_Q4():
    nested_list = [10, [5, None, None], [15, [11, None, None], [22, None, None]]]
    my_tree = create_tree_from_nested_list(nested_list)
    print(my_tree)

    flat_list = [None, 10, 5, 15, None, None, 11, 22]
    my_tree = create_tree_from_flat_list(flat_list)
    print(my_tree)

def test_Q5():
    flat_list = [None, 10, 5, 15, None, None, 11, 22]
    my_tree = create_tree_from_flat_list(flat_list)

    print("Breadth first =", breadth_first(my_tree))
		
def test_Q6():
    flat_list = [None, 42, 31, 67, 6, 39, None, 100, None, None, None, None, None, None, 88]
    my_tree = create_tree_from_flat_list(flat_list)

    print('Original =')
    print(my_tree)

    mirror(my_tree)

    print('Reflected =')
    print(my_tree)


def test_Q7():
    values = [26, 54, 94, 17, 31, 77, 44, 51]

    linear = hashing(values, 13, 'linear', None)
    quadratic = hashing(values, 13, 'quadratic', None)
    double = hashing(values, 13, 'double', 5)

    print('Linear =\n', linear)
    print('Quadratic =\n', quadratic)
    print('Double =\n', double)


def test_Q8():
    print('Tree A')
    my_values = [1, 2, 3, 4, 5, 6, 7]
    result = create_binary_search_tree(my_values)
    print(result)

    print('\nTree B')
    my_values = [1000, 100, 10, 1]
    result = create_binary_search_tree(my_values)
    print(result)

def test_Q9():
    wasted = min_waste(700, [155, 183, 281, 192, 111, 267, 154, 134])
    print('Time left =', wasted)

    wasted = min_waste(100, [50, 20, 10, 39])
    print('Time left =', wasted)



## Display a welcome message
print_welcome()

## Run the tests
print('\n==========================\n==== QUESTION 1 TESTS ====\n==========================')
test_Q1()
print('\n==========================\n==== QUESTION 2 TESTS ====\n==========================')
test_Q2()
print('\n==========================\n==== QUESTION 3 TESTS ====\n==========================')
test_Q3()
print('\n==========================\n==== QUESTION 4 TESTS ====\n==========================')
test_Q4()
print('\n==========================\n==== QUESTION 5 TESTS ====\n==========================')
test_Q5()
print('\n==========================\n==== QUESTION 6 TESTS ====\n==========================')
test_Q6()
print('\n==========================\n==== QUESTION 7 TESTS ====\n==========================')
test_Q7()
print('\n==========================\n==== QUESTION 8 TESTS ====\n==========================')
test_Q8()
print('\n==========================\n==== QUESTION 9 TESTS ====\n==========================')
test_Q9()


