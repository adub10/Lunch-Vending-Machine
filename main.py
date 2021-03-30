class LunchVendingMachine:

  
  def __init__(self,bunsIn,meatIn,ketchupIn,lettuceIn,tomatoesIn,picklesIn,doughIn,sauceIn,CheeseIn,iceCreamIn,bowlsIn,conesIn):
    self.buns = bunsIn
    self.meat = meatIn
    self.ketchup = ketchupIn
    self.lettuce = lettuceIn
    self.tomatoes = tomatoesIn
    self.dough = doughIn
    self.sauce = sauceIn
    self.cheese = CheeseIn
    self.iceCream = iceCreamIn
    self.bowls = bowlsIn
    self.cones = conesIn
    self.pickles = picklesIn


  

  #1 bun, 1 meat patty, 1 ketchup, 2 lettuce, 1 tomato,3pickles
  def makeHamburger(self,quantity):
    if self.buns < quantity or self.meat < quantity or self.ketchup < quantity or self.lettuce < quantity * 2 or self.tomatoes < quantity or self.pickles < quantity * 3:
      return False
    else:
      self.buns -= quantity
      self.meat -= quantity
      self.ketchup -= quantity
      self.lettuce -= quantity * 2
      self.tomatoes -= quantity
      self.pickles -= quantity * 3
      return True

  def makePizza(self,quantity):
    if self.dough < quantity * 2 or self.sauce < quantity or self.cheese < quantity:
      return False
    else:
      self.dough -= quantity * 2
      self.sauce -= quantity
      self.cheese -= quantity
      return True



  def selection(self):
    print("Welcome to the Lunch Machine!")
    print("What do you want today?")
    choice = input ("A - Hamburger  B - Cheese Pizza  C - Ice Cream")

    if choice == "A":
      burgerCount = int(input("How Many Burgers Do You Want?"))
      if self.makeHamburger(burgerCount) == True:
        if burgerCount == 1:
          print("Here is your burger.")
        else:
          print("Here are your burgers.")
      else:
        print("We can't complete that order.")
    if choice == "B":
      pizzaCount = int(input("How Many Pizzas Would You Like?"))
      if self.makePizza(pizzaCount) == True:
        if pizzaCount == 1:
          print ("Enjoy your pizza.")
        else:
          print("Enjoy your pizzas.")
      else:
        print("Sorry, we don't have enough ingredients to finish your order.")
MyVendingMachines = LunchVendingMachine(20,5,6,30,15,7,3,2,8,3,6,8)

MyVendingMachines.selection()