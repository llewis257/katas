'''Create a decorator expected_type() that checks if what the decorated function returns is of expected type. 
An UnexpectedTypeException should be raised if the type returned by the decorated function doesn't match the ones expected.

Requirements:

    expected_type() should accept a tuple of many types that may be valid

    UnexpectedTypeException should be raised if decorated function returns object of type that wasn't defined in expected_type()'s arguments (you have to implement that class)

    return_something will be decorated with expected_type in the tests and will look exactly like in the example below


@expected_type((str,))
def return_something(input):
    # do stuff here with the input...
    return something

##>>> return_something('The quick brown fox jumps over the lazy dog.')
'The quick brown fox jumps over the lazy dog.' 

##>>> return_something('The quick brown fox jumps over the lazy dog.')
'Maybe you'll output another string...'

##>>> return_something(None)
UnexpectedTypeException: Was expecting instance of: str    <<< if the returned type isn't one of the expected ones.
    '''
class UnexpectedTypeException(Exception):
    def __init__(self, expected):
        self.expected = expected
    def __str__(self):
        return f" Was expecting instance of: {self.expected}"

def expected_type(return_types):
    def deco_func(original_func):
        def wrapper_func(*args, **kwargs):
            res = original_func(*args, **kwargs)
            res_check = False
            try:
                res_check = all(i in return_types for i in type(res))
            except TypeError:
                if type(res) in return_types:
                    res_check = True
            if res_check == True:
                return res
            else:
                print(type(res), ' != ', return_types)
                raise UnexpectedTypeException(return_types)
        return wrapper_func
    return deco_func


@expected_type((str,int))
def return_something(inp):
    something = inp
    return something

if __name__ == "__main__":
    return_something('Hello maneee')
    return_something(100)
    return_something(('John', 25))
