x = 10 # int
y = "10" # string
z = 10.1 # float

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

dir(str) # see methods of class
dir(__builtins__) # see standalone functions

grades = [90, 45, 75, 80]
total = sum(grades)
students = len(grades)

avg_grade = total / students
print(avg_grade)