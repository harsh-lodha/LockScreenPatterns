import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result= func(*args,**kwargs)
        end = time.time()
        print(f"Time taken by {func.__name__}: {end - start} seconds")
        return result
    return wrapper

# 1 and 3 position cant be connected unless 2 is already in the pattern. When connecting 1 and 3, it will pass from 2.
# 4213 is a valid 13 connection. 4132 is a invalid 13 connection.
invalid_addition = {
    (1,3):2,
    (1,7):4,
    (1,9):5,
    (2,8):5,
    (3,1):2,
    (3,7):5,
    (3,9):6,
    (4,6):5,
    (6,4):5,
    (7,1):4,
    (7,3):5,
    (7,9):8,
    (8,2):5,
    (9,1):5,
    (9,3):6,
    (9,7):8
}
count = 0
def valid_append(trav_list:list, num):
    if not trav_list:
        return True
    if((trav_list[-1],num) in invalid_addition.keys()):
        val = invalid_addition[(trav_list[-1],num)]
        if val in trav_list:
            return True
        else:
            return False
    return True

def pattern_count(trav_list):
    global count
    for i in set([1,2,3,4,5,6,7,8,9]).difference(set(trav_list)):
        if len(trav_list)<3:
            if valid_append(trav_list,i):
                pattern_count(trav_list+[i])
        else:
            if valid_append(trav_list,i):
                # print("".join(for i in (trav_list+[i]))) # To print patterns
                count = count+1
                pattern_count(trav_list+[i])

@time_it
def abc():
    pattern_count([])

abc()
print(count)
