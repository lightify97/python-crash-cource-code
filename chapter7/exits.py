active = True
while active:
    topping = input("Enter your pizza topping ('quit' to end): ")

    if topping.lower() == 'quit':
        active = False
    else:
        print("Adding {} to your pizza.".format(topping))