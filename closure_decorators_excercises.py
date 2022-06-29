#Closures-Decorators Excercises

#Closure Excercise
#Using a closure, create a function, multiples_of(n) which we can use to
#create generators that generate multiples of n less than a given number.

def multiples_of(number):
    def multiples(count):
        for c in range(number,count,number):
            yield c
    return multiples




m3 = multiples_of(3)
m3_under30 = m3(30)
m7_under30 = multiples_of(7)(30)

print(type(m3_under30))
# output: <class 'generator'>

print(*m3_under30)
# output: 3 6 9 12 15 18 21 24 27

print(*m7_under30)
# output: 7 14 21 28
#----------------------------------------------------------------------

#Decorators Excercise 1
#@make_upper – make every letter of a string returned from the decorated
#function uppercase.
def decorator_for_upper(f):
    def upper_wrapper():
        print(f.upper())
        f()
    return upper_wrapper

def hello_world():
    return 'hello young, good day!!'
f0 = decorator_for_upper(hello_world)
print(f0) # output: HELLO YOUNG, GOOD DAY!!
#-----------------------------------------------------------------------

#Decorators Excercise 2
#@print_func_name – print the name of the decorated function before
#executing the function.
def f1_decorator(f):
    def print_function_name():
        print(f.__name__ + ' is running...')
        f()
    return print_function_name

def my_func():
    print('Python is fun!!')
f1= f1_decorator(my_func)
f1()
#my_func() # output: my_func is running...
            #Python is fun
#----------------------------------------------------------------------

#Decoratos Excercise 3
#@give_name(name) – concatenate the given name at the end of a string
#returned from the decorated function.
def f2_decorator(f):
    def add_name(name):
        def f2_wrapper():
            print(f() + " " + name())
        return f2_wrapper
    return add_name

def name():
    return 'Theresa'

def greeting():
    return 'Hello'
f2=f2_decorator(greeting)(name)
f2()
#print(greeting()) # output: Hello Theresa
#---------------------------------------------------------------------

#Decorators Excercise 4
#@print_input_type – print a data type of the input argument before
#executing the decorated function.
def f3_decorator(f):
    def f3_wrapper(): 
        print( 
            str(type(f)) + " " +
            str(f)
            )
    return f3_wrapper

def square(n):
    return n ** 2

f3=f3_decorator(square(3.5))
f3()

#print(square(3.5)) # output: The input data type is <class 'float'>
                    #12.25
#-------------------------------------------------------------------

#Decorators Excercise 5
#@check_return_type(return_type) – check if the return type of the
#decorated function is return_type and print the result before executing
#the function.

def f4_decorator(f, t):
    def f4_wrapper():
        if type(f)==t:
            print(f"The return type is {t}: {f}")
        else: print(f"Error!! The return type is {t} not {type(f)}")
    return f4_wrapper

#pass in a string
def square(n):
    return n ** 2

print(square(6)) # output: =========Error!!
                    #The return type is NOT <class 'str'>
                    #36
f4=f4_decorator(square(2.9), int)
f4()
#pass in a float
def square(n):
    return n ** 2
f4=f4_decorator(square(2.9), float)
f4()

print(square(2.9)) # output: The return type is <class 'float'>
                    #8.41
#------------------------------------------------------------------------

#Decorators Excercise 6
#@execute_log – write a function execution log on the log file. (log below)
from datetime import datetime

def f5_decorator(f):
    def f5_wrapper(*args):
        print(f"{datetime.now()} {f.__name__} {f(*args)}")
        
    return f5_wrapper

def multiply(*nums):
    mult = 1
    for n in nums:
        mult *= n
    return mult

def hello_world():
    return 'hello world!!'
m = multiply
h = hello_world
type(m)

f5 = f5_decorator(m)
f5()
f5 = f5_decorator(hello_world)
f5()
#print(multiply(6, 2, 3)) # 36
#print(hello_world()) # hello world!!
#print(multiply(2.2, 4)) # 8.8
#print(hello_world()) # hello world!!


#function_execution.log
#2020-05-01 13:55:53.059315 multiply
#2020-05-01 13:55:53.060312 hello_world
#2020-05-01 13:55:53.060314 multiply
#2020-05-01 13:55:53.060323 hello_world