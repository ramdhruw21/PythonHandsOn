def recursion_fun(k):
    if(k>0):
        result = k + recursion_fun(k-1)
        print(result)
    else:
        result = 0
    return result


print("\n\n Recursion Example Results")
recursion_fun(6)