import random

my_wallet = [20]

def greeting():
  print(f"Welcome to the Casino!\nYou have been given a ${sum(my_wallet):.2f} credit.\nCash out at any time.\nIf you run out of money, you can add more.")

slot_machine_values = ['bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bomb', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar', 'bar', '7', '7', '7', '7', '7', '7', 'cherry', 'cherry', 'cherry', 'cherry', 'cherry', 'jackpot', 'jackpot', 'jackpot']
jackpot = ['jackpot', 'jackpot', 'jackpot']
cherry = ['cherry', 'cherry', 'cherry']
seven = ['7', '7', '7']
bar = ['bar', 'bar', 'bar']

def pay_table():
  print("Welcome to the slot machine! Spin the wheel for your chance to win!\nEach spin costs $0.25.\nThe following combinations will result in a win:\n jackpot, jackpot, jackpot: Pays out the grand jackpot of $10,000!\n cherry, cherry, cherry: Pays $100\n 7, 7, 7: Pays $50\n bar, bar, bar: Pays $20\n 2 cherries: Pays $10\n 1 cherry: Pays $1\nGet ready to play!")

def players_option():
  play_or_quit = input("Would you to (S)pin, (C)ash out, or (A)dd to your wallet? ").upper()
  if play_or_quit == 'S':
    cost_of_spin = -0.25
    my_wallet.append(cost_of_spin)
    spin()
  elif play_or_quit == 'C':
    print(f"Your wallet's total is ${sum(my_wallet):.2f}. Thanks for visiting the Casino! See you again soon!")
  elif play_or_quit == 'A':
    amount = input("How much money would you like to add to your wallet? ")
    my_wallet.append(float(amount))
    print(f"Your wallet's total is now ${sum(my_wallet):.2f}.")
    players_option()
  else: 
    print('That is not a valid option. Try again.')
    players_option()

def spin():
  first_item = random.choice(slot_machine_values)
  second_item = random.choice(slot_machine_values)
  third_item = random.choice(slot_machine_values)
  players_spin = [first_item, second_item, third_item]
  print(f"Your spin is: {players_spin}.")

  if players_spin == jackpot:
    my_wallet.append(10000)
    print("You won the jackpot!!")
    players_option()
  elif players_spin == cherry:
    my_wallet.append(100)
    print("You won $100")
    players_option()
  elif players_spin == seven:
    my_wallet.append(50)
    print("You won $50")
    players_option()
  elif players_spin == bar:
    my_wallet.append(20)
    print("You won $20")
    players_option()
  else:
    print("You did not win. Sorry.")
    players_option()


greeting()

pay_table()

players_option()