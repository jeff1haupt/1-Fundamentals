# for i in range(0, 10):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

# for s in ['Avery', 'Kyle', 'Sam', 'Abdou', 'Bob']:
#     if len(s) == 3:
#         print(s)
#         break # this stops the for loop at Sam


# ## writing our own function

# def my_function(name): # function definition and it only runs when we call it
#     print('Hello', name)
#     # code that will run when function is called (DON'T FORGET TO INDENT)

# my_function('Seble') # function call also saying name = 'Seble' 

# def get_area(length, width):
#     return length * width

# area = get_area(10, 10)
# print(area)

# def student_info(name, grade_level, email, age):
#     print(f"The student's name is {name}")
#     print(grade_level + 1)

# student_info('Jeff Haupt', 'Junior', 'example@email.com', 30)

# built in methods
# print(sorted([55, 1234123, 0, -6, 100]))

# print(set([55, -6, 1234123, 0, -6, 100, 0, 0]))

# using functions with input

# selection = input('Enter a number between 1 and 10\n')
# number_given = int(selection)
# print(type(number_given))
# print(type(selection))

# Scope
a = 5
print(a) # 5
def example_1():
    global a
    a = 5 * 5
    print(a) # 25

example_1()
print(a) # 25

a = 5
print(a) # 5
def example_1():
    a = 5 * 5
    return a

a = example_1()
print(a) # 25
