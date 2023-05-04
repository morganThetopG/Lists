import random

total = 0
#The Amazing Waiters
waiters = {
  1: "Morgussy",
  2: "Debs",
  3: "Rylan",
}

#The Menu
menu = {
  "main": ["burger", "amonjus sus", "griddy"],
  "sides": ["ches_quick", "feetpics", "men!?!?!?"],
  "drinks": ["choccy milk", "gamerbathwater", "hairy soup"],
}
list = []


#The Diner
def diner():
  global total
  print("Hiya my name is " + waiters[random.randint(1, 3)] +
        " our main dishes are " + str(menu["main"]) + " which are 4$")
  print("Our sides are " + str(menu["sides"]) + " which are all 2$ " +
        "\n and our drinks are " + str(menu["drinks"]) + " which are 69.42")
  orders()


#how the orders work
def orders():
  global total
  global list
  order = input("Make An Order: ").lower()
  if order == "burger" or order == "amonjus sus" or order == "griddy":
    total += 4
    list.append(order)
    #exit conditnal
    exit = input("Is that all Y/N: ").lower()
    if exit == "y":
      print("Your total is " + str(total) + " And You Ordered" + str(list))
    else:
      print("You've Ordered " + str(list) + " So Far")
      orders()
    #sides
  elif order == "ches_quick" or order == "feetpics" or order == "men!?!?!?":
    total += 2
    list.append(order)
    #exit conditnal
    exit = input("Is that all Y/N: ").lower()
    if exit == "y":
      print("Your total is " + str(total) + " And You Ordered" + str(list))
    else:
      print("You've Ordered " + str(list) + " So Far")
      orders()
  #drinks
  elif order == "gamerbathwater" or order == "choccy milk" or order == "hairy soup":
    total += 69.42
    list.append(order)
    #exit conditnal
    exit = input("Is that all Y/N: ").lower()
    if exit == "y":
      print("Your total is " + str(total) + " And You Ordered" + str(list))
    else:
      print("You've Ordered " + str(list) + " So Far")
      orders()
  #if you type something not avalible
  else:
    print("Sorry We Dont Have That ")
    orders()


diner()