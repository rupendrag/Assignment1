def outer_function(A, B):
    def inner_function():
        return A + B
    
    addition_result = inner_function() + 5
    return addition_result

result = outer_function(3, 7)
print("Result:",result)