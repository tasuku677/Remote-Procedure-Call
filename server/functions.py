import math
def floor(params):
    return {
        "type": "int",
        "value":math.floor(params[0])
    }

def nroot(params):
    x = params[0]
    n = params[1]
    return {
        "type": "float",
        "value": x ** (1 / n)
    }

def validAnagram(params):
    if params[0].sort == params[1].sort:
        return{
            "type": "bool",
            "value": True
        }
    else:
        return{
            "type": "bool",
            "value": False
        }
    
def reverse(params):
    return {
            "type": "string",
            "value": params[0][::-1]
    }

def sort(params):
    return {
        "type": "string",
        "value": ''.join(sorted(params[0]))
    }

def check_params(method, params_types):
    if method == 'floor':
        if params_types[0] == 'float':
            return True
    elif method == 'nroot':
        if params_types[0] == 'int' and params_types[1] == 'int':
            return True
    elif method == 'validAnagram':
        if params_types[0] == 'string' and params_types[1] == 'string':
            return True
    elif method == 'reverse':
        if params_types[0] == 'string':
            return True
    elif method == 'sort':
        if params_types[0] == 'string':
            return True
    else:
        return False
    return False
