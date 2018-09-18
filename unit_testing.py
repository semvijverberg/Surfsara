print('something')

# After you changed something, your code can produce an error down-the-line, 
# which you did not anticipate. To avoid these kind of errors, you do unit-testing

# unit testing is to check if you code still works for the entire 
# input variable range. 



a = 1
assert type(a) == int

# not yet unit testing, but conservative programming
def sum(a,b):
    assert type(a) == int, "b is not an int"
    assert type(b) == int, "b is not an int"
    return a + b

sum(4, '5')

def awesome_function():
    print('Do some heavy calculation')
    return 42


