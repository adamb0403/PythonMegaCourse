def foo1(lst):
    return [x if isinstance(x, int) else 0 for x in lst]

def foo2(lst):
    return [x for x in lst if x > 0]

def foo3(lst):
    new_lst = [float(x) for x in lst]
    print(sum(new_lst))
# my_list = [24, 454, 64, 2, 6565, 34, 7567, "hi", "jkds", "no"]
# new_list = [number for number in my_list if isinstance(number, int)]

foo3(['1.2', '2.6', '3.3'])