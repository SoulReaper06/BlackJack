import random 

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#function to calculate final score 
def gameOver(playerScore, cpuScore,choice):
  """This function takes in both decks and user's choice ,then prints the sum of cards and checks if
     value goes over 21
  """
  print(f"Your cards: {playerScore} , current score: {sum(playerScore)}")
  print(f"Computer's Card : {cpuScore}, current score: {sum(cpuScore)}")
  if(choice == "y"):      
    if(sum(playerScore) > 21):
      print("Busted !! , Try Again")
    else:
      print("You Win !!")
  else:
    if(sum(player_Deck) > sum(cpu_deck)):
      print("You Win")
    else:
      print("CPU WINS !!!")  

# function to add 11 or 1 as per the current score (sum of deck)          
def checkAce(deck):
  if(11 in deck):
    if(sum(deck) > 21):
      deck.remove(11)
      deck.append(1)
  return deck    
  

startGame = input("Do you want to play a game of BlackJack ? Type yes or no : ").lower()
if(startGame == "yes"):
  print(logo)

  deck = [11, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
  player_Deck = []
  cpu_deck = []

  for _ in range(2):
    player_Deck.append(random.choice(deck))
    cpu_deck.append(random.choice(deck))

  player_Deck = checkAce(player_Deck)
  cpu_deck = checkAce(cpu_deck)
  print(f"Your cards: {player_Deck} , current score: {sum(player_Deck)}")
  print(f"Computer's Card : {cpu_deck[0]}")
  play = "y"
  while play == "y":
    play = input("Type y to get another card, type n to pass : ")
    if(play == "y"):
      player_Deck.append(random.choice(deck))
      cpu_deck.append(random.choice(deck))
      player_Deck = checkAce(player_Deck)
      cpu_deck = checkAce(cpu_deck)
      if( sum(player_Deck) > 21 or sum(cpu_deck) > 21):
        gameOver(player_Deck,cpu_deck,choice="y")
        break
      print(f"Your cards: {player_Deck} , current score: {sum(player_Deck)}")
      print(f"Computer's Card : {cpu_deck[0]}")   
    else:
      gameOver(player_Deck,cpu_deck,choice="n")
else:          
  print("GOODBYE !!")
      

