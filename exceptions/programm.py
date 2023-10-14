result = []
def divider(a, b):
    if a < b :
        raise ValueError("ValueError")
    if b > 100:
        raise IndexError("IndexError")
    return a/b
data = {10: 2, 5: 5, "123": 4, 18: 0,tuple([]):10, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except TypeError:
        if type(key) is str:
            print(f"Error.You cant divide '{key}' by {data[key]}.Because '{key}' is string data type")
        else:
            print(f"Error.You cant divide {list(key)} by {data[key]}.")
    except ZeroDivisionError:
        print(f"You cant divide {key} by {data[key]}.Because it is impossible to divide by zero.")
print(result)

    
