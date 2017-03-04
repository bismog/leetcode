# https://www.programiz.com/python-programming/function-argument
# Python allows functions to be called using keyword arguments. When we call 
# functions in this way, the order (position) of the arguments can be changed.
# As we can see, we can mix positional arguments with keyword arguments during
# a function call. But we must keep in mind that keyword arguments must follow 
# positional arguments.
def greet(name, msg = "Good morning!"):
    """
    This function greets to the person with the provided message.
    If message is not provided, it defaults to "Good morning!"
    """

    print("Hello", name + ', ' + msg)

greet(name = "Bruce", msg = "How do you do?")
greet(msg = "How do you do?", name = "Bruce")
greet("Bruce", msg = "How do you do?")
