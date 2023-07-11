def string_calcuation(mystring):
    interrogatives = ("how", "what", "why", "where", "who")
    new_string = mystring.capitalize()
    if mystring.startswith(interrogatives):
        return "{}?".format(new_string)
    else:
        return "{}.".format(new_string)

results = []

while True:
    input_string = input("Say something: ")
    if input_string == "\end":
        break
    results.append(string_calcuation(input_string))

print(" ".join(results))