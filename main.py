import random

my_wallet = [20]

def greeting():
  print(f"Welcome to the Casino!\nYou have been given a ${sum(my_wallet):.2f} credit.\nCash out at any time.\nIf you run out of money, you can add more.")

slot_machine_values = ['bar', '7', 'cherry', 'jackpot']

def pay_table():
  print("Welcome to the slot machine! Spin the wheel for your chance to win!\nEach spin costs $1.\nThe following combinations will result in a win:\n jackpot, jackpot, jackpot: Pays out the grand jackpot of $1,000!\n cherry, cherry, cherry: Pays $100\n 7, 7, 7: Pays $50\n bar, bar, bar: Pays $20\n 2 cherries: Pays $10\n 1 cherry: Pays $1\n Get ready to play!")

def players_option():
  play_or_quit = input("Would you to (S)pin or (C)ash out? ").upper()
  print(play_or_quit)
  if play_or_quit == 'S':
    spin()
  elif play_or_quit == 'C':
    print(f"Your wallet's total is ${sum(my_wallet)}. Thanks for visiting the Casino! See you again soon!")
  else: 
    print('That is not a valid option. Try again.')
    players_option()


greeting()

pay_table()

players_option()