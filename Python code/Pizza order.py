#Define a function to add the delivery cost and order details
def delivery(total):

    choice = input("Delivery or pick up:\n")
    choice = choice.lower()
    
    if choice == "delivery":
        total = total + 2.50
        address = input("What is your address?:\n")

    elif choice == "pick up":
        total = total + 0
        name = input("What is your name?:\n")
        
    else:
        print("Your input was incorrect please retry")
        delivery(total)
    return total

def toppings(total):

    numberOfToppings = 0
    toppingList = "Pick One:\nextra-cheese,pepperoni,sausage,ham,beef,onion,mushrooms,pineapple,peppers,olives"

    print("First Three Toppings are FREE, extras are $0.45 per topping")    

    cheesePizza = input("do you want toppings?: (Y)es or (N)o\n")

    incorrect = 1
    while incorrect == 1:
        if (cheesePizza.lower() == "n") | (cheesePizza.lower() == "no"):
            return total
        elif (cheesePizza.lower() == "y") | (cheesePizza.lower() == "yes"):
            choice = "y"
            incorrect = 0 
        else:
            print("incorrect list entry, try again")
            cheesePizza = input("do you want toppings?: (Y)es or (N)o\n")
        
    while choice.lower() == "y":
        topping = input(toppingList)

        while toppingList.find(topping) == -1:
            print("incorrect list entry, try again")
            topping = input(toppingList)
            
        toppingList = toppingList.replace(topping + ',','')
        
        choice = input("Do you want more toppings: (Y)es or (N)o\n")
        while (choice.lower() != "y") & (choice.lower() != "n"):
            print("incorrect input stephanie")
            choice = input("Do you want more toppings: (Y)es or (N)o\n") 

        numberOfToppings = numberOfToppings + 1
        if numberOfToppings > 3:
            total = total + (0.45 * 1.06)
               
    return total

def pizzaSize(total):

    size = input("ByTheSlice ($1.75) or 12in ($10.50) or 16in ($15.00)\n")

    if size.lower() == "bytheslice":

        numberOfSlices = int(input("How Many?\n"))        
        for i in range(numberOfSlices):
            total = total + (1.75 * 1.06)

    elif size.lower() == "12in":
        total = total + (10.50 * 1.06)
    elif size.lower() == "16in":
        total = total + (15.00 * 1.06)
    else:
        print("Incorrect input: please try again")
        pizzaSize(total)    
    return total

def pizzaCrust(total):

    crust = input("Thin ($0) or DeepDish ($1.00)\n")
    if crust.lower() == "deepdish":
        total = total + (1.00 * 1.06)
    elif crust.lower() == "thin":
        total = total + 0        
    else:
        print("Incorrect input: please try again")
        pizzaCrust(total)    
    return total

    
def main():
    
    total = 0
    total = delivery(total)
    total = pizzaCrust(total)
    total = pizzaSize(total)
    total = toppings(total)
    print("your total is ${0:.2f}".format(total))

    creditNumber = input("what is your Credit Card number?\n")
    
    return


main()
