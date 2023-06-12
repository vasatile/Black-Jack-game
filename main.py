############### Blackjack Project #####################
import random
from replit import clear
from art import logo





def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  sum(cards)
 
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    

  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "you lose your opponent has a Black jack"
  elif user_score == 0:
    return "You win, you have a black jack"
  elif user_score > 21:
    return " you lose you went over 21"
  elif computer_score > 21:
    return " you win oppenent score went over 21"
  elif user_score > computer_score:
    return "you win"
  else:
    return "You lose"
  

  

  
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    
    
    
    
    
    
    print(f" your cards: {user_cards} and score is {user_score}")
    print(f" computer's cards: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
     user_should_deal =  input("do you want to get another card? type 'y' for another card. type 'n' to pass ")
    if user_should_deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f" your final hand is {user_cards} and final score {user_score}")
  print(f" computer's final hand is {computer_cards} and final score {computer_score}")
  print(compare(user_score, computer_score))







while input(" do you want to play game of BlackJack? type 'y' for yes and 'n' for no \n") == "y":
  clear()
  play_game()
