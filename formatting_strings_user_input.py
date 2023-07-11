def greetings(name):
    return("Hi {}".format(name.capitalize()))
    
input_name = input("Enter your name: ")
print(greetings(input_name))