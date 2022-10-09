import random

def highlight(func):
    annotations = ['-', '*', '+', ':', '^']
    annotate = random.choice(annotations)
    print(annotate * 30)
    func()
    print(annotate * 30)


@highlight  # here calling the another function with '@function name', here highlight() function is taking print_msg() as input argument
def print_msg():
    print("Now the message is decorated")

