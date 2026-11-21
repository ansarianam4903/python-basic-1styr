# 12.compute the length of given list or string

def find_length(data):
    count = 0
    for _ in data:
        count +=1
    return count 


# Test 
print(find_length("Hellollllll1"))
print(find_length([1, 2, 3, 4]))
