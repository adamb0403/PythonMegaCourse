def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return(the_mean)

def area(side_length):
    the_area = side_length**2
    return(the_area)

def volume_converter(ounces):
    milliliters = ounces * 29.57353
    return milliliters

def new_mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

# print(mean([1,4,6,7]))
# print(area(25))

temps = [3.5, 4.6, 5.3, 23.6]
grades = {"Adam": 25, "James": 46, "John": 35}

print(new_mean(temps))
print(new_mean(grades))