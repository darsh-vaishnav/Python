
# # ============================================================
# # PYTHON FUNCTIONS — 20 MIXED PRACTICE QUESTIONS
# # Topics: /, *, *args, **kwargs, parameter order, edge cases
# # Instructions: Predict the output before checking the answer.
# # ============================================================


# # Q1. What is the output?

# def show(*args):
#     print(args)

# show(10, 20, 30)

# # Answer: (10, 20, 30)


# # Q2. What happens?

# def add(a, b, /):
#     return a + b

# print(add(a=3, b=4))

# # Answer: TypeError
# # Reason: a and b are positional-only.


# # Q3. What is the output?

# def greet(name, *, message="Hi"):
#     print(message, name)

# greet("Darsh")

# # Answer: Hi Darsh


# # Q4. What is the output?

# def show(name, *values):
#     print(name)
#     print(values)

# show("Asha", 5, 10)

# # Answer:
# # Asha
# # (5, 10)


# # Q5. What is the output?

# def profile(**kwargs):
#     print(kwargs)

# profile(name="Asha", age=20)

# # Answer: {'name': 'Asha', 'age': 20}


# # Q6. What is the output?

# def show(*args):
#     print(len(args))

# show()

# # Answer: 0


# # Q7. What happens?

# def show(a, b):
#     print(a, b)

# show(1, 2, 3)

# # Answer: TypeError
# # Reason: Too many positional arguments.


# # Q8. What is the output?

# def demo(a, /, b):
#     print(a, b)

# demo(10, b=20)

# # Answer: 10 20


# # Q9. What is the output?

# def show(*args):
#     print(args)

# show(*[2, 4, 6])

# # Answer: (2, 4, 6)
# # Reason: The list is unpacked into separate arguments.


# # Q10. What happens?

# def show(*, x):
#     print(x)

# show(5)

# # Answer: TypeError
# # Reason: x is keyword-only; use show(x=5).


# # Q11. What is the output?

# def show(a, *args, option=True):
#     print(a, args, option)

# show(1, 2, 3, option=False)

# # Answer: 1 (2, 3) False


# # Q12. What happens?

# def show(a, **kwargs):
#     print(a, kwargs)

# show(1, a=2)

# # Answer: TypeError
# # Reason: a receives two values.


# # Q13. What is the output?

# def show(*args):
#     print(args)

# show(*"OK")

# # Answer: ('O', 'K')


# # Q14. What is the output?

# def show(**kwargs):
#     print(kwargs.get("city", "Unknown"))

# show(name="Asha")

# # Answer: Unknown


# # Q15. Which definition causes a SyntaxError?

# # A. def f(a, /, b): pass
# # B. def f(*args, option=True): pass
# # C. def f(a, *, b): pass
# # D. def f(**kwargs, *args): pass

# # Answer: D
# # Reason: **kwargs must appear last.


# # Q16. What is the output?

# def show(*args):
#     print(args)

# show([1, 2])

# # Answer: ([1, 2],)
# # Reason: Without unpacking, the list is one argument.


# # Q17. What happens?

# def show(name):
#     print(name)

# show(name="A", age=20)

# # Answer: TypeError
# # Reason: age is not an accepted parameter.


# # Q18. What is the output?

# def show(pos, /, **kwargs):
#     print(pos, kwargs)

# show(1, pos=9)

# # Answer: 1 {'pos': 9}


# # Q19. What is the output?

# def show(a, b=5, *args):
#     print(a, b, args)

# show(1, 2, 3, 4)

# # Answer: 1 2 (3, 4)


# # Q20. What is the output?

# def show(a, /, b, *, c=3, **kwargs):
#     print(a, b, c, kwargs)

# show(1, b=2, d=4)

# # Answer: 1 2 3 {'d': 4}


# # ============================================================
# # QUICK REVISION
# # ============================================================

# # args       = normal parameter name
# # *args      = collects extra positional arguments into a tuple
# # **kwargs   = collects extra keyword arguments into a dictionary
# # *          = makes following parameters keyword-only
# # /          = makes preceding parameters positional-only
# # *list      = unpacks an iterable into positional arguments
# # **dict     = unpacks a dictionary into keyword arguments
# # TypeError  = commonly raised for invalid function calls
# # SyntaxError = raised for invalid Python syntax



# # ============================================================
# # PYTHON FUNCTION PARAMETERS: COMPLETE NOTES
# # Topics: /, *, *args, **kwargs, parameter order, edge cases
# # ============================================================


# # ============================================================
# # 1. POSITIONAL-ONLY PARAMETERS: /
# # ============================================================

# # Parameters before / must be passed by position.

# def divide(a, b, /):
#     return a / b

# print(divide(10, 2))             # 5.0
# # divide(a=10, b=2)              # TypeError
# # divide(10, b=2)                # TypeError
# # divide()                       # TypeError
# # divide(10, 2, 3)               # TypeError


# # Positional-only + regular parameter

# def calculate(a, b, /, operation="add"):
#     if operation == "add":
#         return a + b
#     elif operation == "multiply":
#         return a * b
#     return None

# print(calculate(3, 4))                       # 7
# print(calculate(3, 4, "multiply"))           # 12
# print(calculate(3, 4, operation="multiply")) # 12


# # Positional-only parameter name can appear in **kwargs

# def show(name, /, **kwargs):
#     print(name)
#     print(kwargs)

# show("Darsh", name="Python")
# # Darsh
# # {'name': 'Python'}


# # ============================================================
# # 2. KEYWORD-ONLY PARAMETERS: BARE *
# # ============================================================

# # Parameters after a bare * must be passed by keyword.

# def create_user(name, *, age, city):
#     return f"{name}, age {age}, from {city}"

# print(create_user("Asha", age=20, city="Pune"))
# # Asha, age 20, from Pune

# # create_user("Asha", 20, "Pune")  # TypeError
# # create_user("Asha", age=20)      # TypeError: city missing


# # Keyword-only parameter with a default

# def greet(name, *, message="Hello"):
#     print(message, name)

# greet("Darsh")                    # Hello Darsh
# greet("Darsh", message="Welcome") # Welcome Darsh


# # Keyword arguments can be given in any order

# def profile(*, name, age, city):
#     print(name, age, city)

# profile(city="Ahmedabad", age=20, name="Darsh")


# # ============================================================
# # 3. USING / AND * TOGETHER
# # ============================================================

# def book_ticket(source, destination, /, *, passenger, seat="regular"):
#     print(source, "to", destination)
#     print("Passenger:", passenger)
#     print("Seat:", seat)

# book_ticket("Pune", "Mumbai", passenger="Asha", seat="window")
# book_ticket("Pune", "Mumbai", passenger="Darsh")

# # source, destination: positional-only
# # passenger, seat: keyword-only
# # seat is optional because it has a default value


# # Regular parameter between / and *

# def order(item, /, quantity, *, discount=0):
#     print(item, quantity, discount)

# order("Pizza", 2, discount=10)
# order("Pizza", quantity=3, discount=5)

# # order(item="Pizza", quantity=2)  # TypeError
# # order("Pizza", 2, 10)            # TypeError
# # order("Pizza")                  # TypeError


# # ============================================================
# # 4. *args: MULTIPLE POSITIONAL ARGUMENTS
# # ============================================================

# # *args collects extra positional arguments into a tuple.
# # The name 'args' is a convention, not a keyword.

# def display(*args):
#     print(args)
#     print(type(args))

# display()
# # ()
# # <class 'tuple'>

# display(10)
# # (10,)

# display(10, 20, 30)
# # (10, 20, 30)


# # Adding values using *args

# def add_all(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total

# print(add_all(10, 20))       # 30
# print(add_all(1, 2, 3, 4))   # 10
# print(add_all())             # 0


# # Regular parameter before *args

# def introduce(name, *hobbies):
#     print("Name:", name)
#     print("Hobbies:", hobbies)

# introduce("Asha", "reading", "cricket", "music")
# # Name: Asha
# # Hobbies: ('reading', 'cricket', 'music')

# # introduce()  # TypeError: name is required


# # *args followed by a keyword-only parameter

# def student(name, *marks, passed=True):
#     print(name)
#     print(marks)
#     print(passed)

# student("Darsh", 80, 90, 95, passed=False)
# # Darsh
# # (80, 90, 95)
# # False


# # Different data types inside *args

# def show_values(*values):
#     print(values)

# show_values("Python", 100, True, None)
# # ('Python', 100, True, None)


# # A custom name works too

# def show_numbers(*numbers):
#     print(numbers)

# show_numbers(1, 2, 3)  # (1, 2, 3)


# # ============================================================
# # 5. *args EDGE CASES
# # ============================================================

# # Passing a list WITHOUT unpacking: one argument

# def show(*args):
#     print(args)

# show([10, 20, 30])
# # ([10, 20, 30],)


# # Passing a list WITH unpacking: separate arguments

# numbers = [10, 20, 30]
# show(*numbers)
# # (10, 20, 30)


# # Unpacking a tuple

# def add_three(a, b, c):
#     print(a + b + c)

# numbers = (10, 20, 30)
# add_three(*numbers)  # 60


# # Default regular parameter + *args

# def show(name="Guest", *args):
#     print(name, args)

# show()                  # Guest ()
# show("Darsh", 10, 20)   # Darsh (10, 20)


# # Duplicate assignment to a regular parameter

# def show(name, *args):
#     print(name, args)

# # show("Darsh", name="Asha")  # TypeError


# # Keyword arguments are not collected by *args

# def display(*args):
#     print(args)

# # display(10, 20, city="Pune")  # TypeError


# # Empty iterable unpacking

# display(*[])  # ()


# # A string is unpacked character by character

# display(*"CAT")  # ('C', 'A', 'T')


# # A dictionary unpacked with * gives its keys

# display(*{"name": "Darsh", "age": 20})
# # ('name', 'age')


# # A single-element tuple requires a comma

# print((10,))  # (10,)


# # ============================================================
# # 6. **kwargs: MULTIPLE KEYWORD ARGUMENTS
# # ============================================================

# # **kwargs collects extra keyword arguments into a dictionary.

# def show_profile(**kwargs):
#     print(kwargs)

# show_profile(name="Darsh", age=20, city="Ahmedabad")
# # {'name': 'Darsh', 'age': 20, 'city': 'Ahmedabad'}


# # Accessing dictionary values

# def profile(**kwargs):
#     print(kwargs["name"])
#     print(kwargs["age"])

# profile(name="Darsh", age=20)


# # Safe access with .get()

# def profile(**kwargs):
#     print(kwargs.get("city", "Unknown"))

# profile(name="Darsh")
# # Unknown


# # *args and **kwargs together

# def display(*args, **kwargs):
#     print(args)
#     print(kwargs)

# display(10, 20, name="Darsh", city="Pune")
# # (10, 20)
# # {'name': 'Darsh', 'city': 'Pune'}


# # Regular parameter + *args + **kwargs

# def student(name, *marks, **details):
#     print(name)
#     print(marks)
#     print(details)

# student("Darsh", 80, 90, age=20, city="Pune")
# # Darsh
# # (80, 90)
# # {'age': 20, 'city': 'Pune'}


# # Unpacking a dictionary with **

# def show_person(name, age):
#     print(name, age)

# data = {"name": "Darsh", "age": 20}
# show_person(**data)  # Darsh 20


# # Missing dictionary key with [] causes KeyError

# def show_city(**kwargs):
#     # print(kwargs["city"])  # KeyError if city is missing
#     print(kwargs.get("city", "Unknown"))

# show_city()


# # ============================================================
# # 7. ALL PARAMETER TYPES TOGETHER
# # ============================================================

# def example(pos_only, /, normal, *args, option=True, **kwargs):
#     print("Positional-only:", pos_only)
#     print("Regular:", normal)
#     print("Extra positional:", args)
#     print("Option:", option)
#     print("Extra keywords:", kwargs)

# example(1, 2, 3, 4, option=False, color="blue")

# # Positional-only: 1
# # Regular: 2
# # Extra positional: (3, 4)
# # Option: False
# # Extra keywords: {'color': 'blue'}


# # Duplicate assignment to a regular parameter

# def example(pos_only, /, normal, **kwargs):
#     print(pos_only, normal, kwargs)

# # example(1, 2, normal=3)  # TypeError


# # A keyword matching a positional-only parameter

# def example(pos_only, /, **kwargs):
#     print(pos_only, kwargs)

# example(1, pos_only=99)
# # 1 {'pos_only': 99}


# # ============================================================
# # 8. VALID PARAMETER ORDER
# # ============================================================

# # Order:
# # 1. Positional-only parameters, followed by /
# # 2. Regular parameters
# # 3. *args or a bare *
# # 4. Keyword-only parameters
# # 5. **kwargs

# def one(a, /, b, *, c):
#     pass

# def two(a, *args, option=True):
#     pass

# def three(a, /, b, *args, option=True, **kwargs):
#     pass

# def four(*args, **kwargs):
#     pass


# # INVALID DEFINITIONS: SYNTAX ERRORS
# # Uncomment ONE at a time to test.

# # def invalid(*args, b, /):
# #     pass
# # / cannot appear after *args.

# # def invalid(**kwargs, *args):
# #     pass
# # *args cannot appear after **kwargs.

# # def invalid(*, a, /):
# #     pass
# # / cannot appear after a bare *.

# # def invalid(a, /, b, /):
# #     pass
# # / cannot be used twice.


# # ============================================================
# # 9. DUPLICATE ARGUMENTS AND UNPACKING ERRORS
# # ============================================================

# def greet(name):
#     print(name)

# # greet(name="Darsh", name="Asha")
# # SyntaxError: duplicate keyword in a direct call


# # Duplicate value when unpacking a dictionary

# data = {"name": "Darsh"}

# # greet(**data, name="Asha")
# # TypeError: multiple values for name


# # Too many positional arguments

# def show_two(a, b):
#     print(a, b)

# # show_two(10, 20, 30)  # TypeError


# # Unexpected keyword argument

# def show_name(name):
#     print(name)

# # show_name(name="Darsh", age=20)  # TypeError


# # Too many arguments after unpacking

# numbers = [10, 20, 30]

# # show_two(*numbers)  # TypeError


# # Empty iterable with *args

# def count_args(*args):
#     print(len(args))

# count_args(*[])  # 0


# # ============================================================
# # 10. IMPORTANT DIFFERENCES
# # ============================================================

# # args: ordinary parameter name
# # *args: collects positional arguments into a tuple
# # **kwargs: collects keyword arguments into a dictionary
# # *: marks following parameters as keyword-only
# # /: marks preceding parameters as positional-only
# # *values in a CALL: unpacks an iterable
# # **data in a CALL: unpacks a mapping into keyword arguments


# # Example: args without *

# def ordinary(args):
#     print(args)

# ordinary(10)  # 10
# # ordinary(10, 20)  # TypeError


# # Example: *args

# def multiple(*args):
#     print(args)

# multiple(10, 20)  # (10, 20)


# # Example: **kwargs

# def keywords(**kwargs):
#     print(kwargs)

# keywords(name="Darsh", age=20)
# # {'name': 'Darsh', 'age': 20}


# # Example: bare *

# def keyword_only(*, age):
#     print(age)

# keyword_only(age=20)  # 20
# # keyword_only(20)  # TypeError


# # Example: /

# def positional_only(age, /):
#     print(age)

# positional_only(20)  # 20
# # positional_only(age=20)  # TypeError


# # ============================================================
# # 11. QUICK MCQ / OUTPUT-PREDICTION PRACTICE
# # ============================================================

# # Q1
# def q1(*args):
#     return type(args).__name__

# print(q1(1, 2))  # tuple


# # Q2
# def q2(a, /):
#     print(a)

# # q2(a=10)  # TypeError


# # Q3
# def q3(*, x=5):
#     print(x)

# q3()  # 5


# # Q4
# def q4(a, *args):
#     print(a, args)

# q4(1, 2, 3)  # 1 (2, 3)


# # Q5
# def q5(a, **kwargs):
#     print(a, kwargs)

# # q5(1, a=2)  # TypeError


# # Q6
# def q6(*args):
#     print(args)

# q6(*[4, 5])  # (4, 5)


# # Q7
# def q7(**kwargs):
#     print(kwargs)

# q7(city="Pune", age=20)
# # {'city': 'Pune', 'age': 20}


# # Q8: Invalid parameter order
# # def q8(a, **kwargs, *args):
# #     pass
# # SyntaxError


# # ============================================================
# # FINAL REVISION
# # ============================================================

# # /        = positional-only
# # *        = keyword-only marker
# # *args    = extra positional arguments -> tuple
# # **kwargs = extra keyword arguments -> dictionary
# # args     = ordinary variable name
# # *list    = unpack iterable into positional arguments
# # **dict   = unpack mapping into keyword arguments

