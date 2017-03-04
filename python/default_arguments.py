# https://www.programiz.com/python-programming/function-argument
# We can provide a default value to an argument by using the assignment 
# operator (=). 
def greet(name, msg = "Good morning!"):
    """
    This function greets to the person with the provided message.
    If message is not provided, it defaults to "Good morning!"
    """

    # print("1.2..3...", "1" + "2" + "3")
    # print("1.2..3...", "1" , "2" , "3")
    # print("1.2..3..."+ "1" + "2" + "3")
    # print("1.2..3..."+ "123")
    # print("1.2..3...", "123")
    print("Hello", name + ', ' + msg)

greet("Kate")
greet("Bruce", "How do you do?")
