import numpy as np

my_wallet = [3]

def greeting():
  print(f"\nWelcome to the Casino!\nYou have been given a ${sum(my_wallet):.2f} credit.\nCash out at any time.\nIf you run out of money, you can add more.")

def pay_table():
  print("\nPlay the slot machine! Spin the wheel for your chance to win!\nEach spin costs $0.25.\nThe following combinations will result in a win:\n \n -jackpot, jackpot, jackpot: Pays out the grand jackpot of $10,000!\n -cherry, cherry, cherry: Pays $100\n -7, 7, 7: Pays $50\n -bar, bar, bar: Pays $20\n -Any combination with 2 cherries: Pays $5\n -Any combination with 1 cherry: Pays $1\n \nGet ready to play!")

jackpot = ['jackpot', 'jackpot', 'jackpot']
cherry = ['cherry', 'cherry', 'cherry']
seven = ['7', '7', '7']
bar = ['bar', 'bar', 'bar']

def players_option():
  play_or_quit = input("\nWould you like to (S)pin, (C)ash out, (V)iew your wallet's balance, or (A)dd to your wallet? ").upper()
  if play_or_quit == 'S':
    check_wallet_balance()
  elif play_or_quit == 'C':
    cash_out()
  elif play_or_quit == 'V':
    print(f"\nYour wallet's balance is ${sum(my_wallet):.2f}.")
    players_option()
  elif play_or_quit == 'A':
    add_money()
  else: 
    print('\nThat is not a valid option. Try again.')
    players_option()

def check_wallet_balance():
  if sum(my_wallet) >= 0.25:
    cost_of_spin = -0.25
    my_wallet.append(cost_of_spin)
    spin()
  else:
    print("\nYou do not have enough money to play the slot machine. Please add more money to your wallet.")
    add_money()

def add_money():
  amount = input("\nHow much money would you like to add to your wallet?\n (1)$5.00\n (2)$10.00\n (3)$20.00\n (4)Return to slot machine. ")
  if amount == '1':
    my_wallet.append(5)
    print(f"\nYour wallet's total is now ${sum(my_wallet):.2f}.")
    players_option()
  elif amount == '2':
    my_wallet.append(10)
    print(f"\nYour wallet's total is now ${sum(my_wallet):.2f}.")
    players_option()
  elif amount == '3':
    my_wallet.append(20)
    print(f"\nYour wallet's total is now ${sum(my_wallet):.2f}.")
    players_option()
  elif amount == '4':
    players_option()
  else:
    print("\nThat is not a valid selection. Try again.")
    add_money()

def spin():
  choices = ['bomb', 'bar', '7', 'cherry', 'jackpot']
  weights = [0.60, 0.18, 0.15, 0.06, 0.01]
  first_item = np.random.choice(choices, p=weights)
  second_item = np.random.choice(choices, p=weights)
  third_item = np.random.choice(choices, p=weights)
  players_spin = [first_item, second_item, third_item]
  print(f"\nYour spin is:\n{(', '.join(players_spin))}")

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
  elif first_item == 'cherry' and second_item == 'cherry' and third_item != 'cherry':
    my_wallet.append(5)
    print("You won $5")
    players_option()
  elif first_item == 'cherry' and second_item != 'cherry' and third_item == 'cherry':
    my_wallet.append(5)
    print("You won $5")
    players_option()
  elif first_item != 'cherry' and second_item == 'cherry' and third_item == 'cherry':
    my_wallet.append(5)
    print("You won $5")
    players_option()
  elif first_item == 'cherry' and second_item != 'cherry' and third_item != 'cherry':
    my_wallet.append(1)
    print("You won $1.")
    players_option()
  elif first_item != 'cherry' and second_item == 'cherry' and third_item != 'cherry':
    my_wallet.append(1)
    print("You won $1.")
    players_option()
  elif first_item != 'cherry' and second_item != 'cherry' and third_item == 'cherry':
    my_wallet.append(1)
    print("You won $1.")
    players_option()  
  else:
    print("You did not win. Sorry.")
    players_option()

def cash_out():
  confirm = input("\nAre you sure you want to cash out? (Y)es or (N)o ").upper()
  if confirm == 'Y':
    print(f"\nThank you for coming to the casino today! Your wallet's balance is ${sum(my_wallet):.2f}. See you again soon!\n")
  elif confirm == 'N':
    players_option()
  else:
    print("\nNot a valid selection. Try again.")
    cash_out()
    
    
greeting()

pay_table()

players_option()