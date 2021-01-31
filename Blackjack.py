import random
from art import logo

#function to get players cards total
def player_total():
  player_cards_total = 0
  for card in players_cards:
    player_cards_total += card
  return player_cards_total

#function to get cpu cards total
def cpu_total():
  cpu_cards_total = 0
  for card in cpu_cards:
    cpu_cards_total += card
  return cpu_cards_total

#function to see who wins
def winner():
  total = player_total()
  cpu_cards_total = cpu_total() 
  if cpu_cards_total > 21 or cpu_cards_total < total:
    return (f"The computer has {cpu_cards_total}, and you have {total}. \n\nYou win :)")
  elif cpu_cards_total == total:
    return (f"You both have {total}, It is a draw!")
  elif cpu_cards_total > total:
    return (f"The computer has {cpu_cards_total}, and you have {total}. \n\nYou lose :(")

play_again = True
while play_again:
    print(logo)
    print("Welcome to BlackJack!\n")

    #List of cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    #Assigning the player and the computer random cards of the list
    players_cards = [random.choice(cards), random.choice(cards)]

    print(f"Your starting cards are {players_cards}")

    cpu_cards = [random.choice(cards), random.choice(cards)]

    print(f"The only card from the computer you see is {cpu_cards[0]}\n")

    #Check to see if player got winning hand
    total = player_total()
    cpu_cards_total = cpu_total()

    if total == 21:
      print("You drew 21 with your first two cards and won!")
    else:
      print(f"Your cards currently add up to {total}")

    #Starting loop for hit me
      hit_me = True

      while hit_me:
        choice = input("Want another card? (y or n) \n")
        if choice == "y":
          players_cards.append(random.choice(cards))
          print(players_cards)
          #If player goes over 21, automatic lost
          if player_total() > 21:
            if 11 in players_cards:
              ace = players_cards.index(11)
              players_cards[ace] = 1
              print("Since you went over 21, your ace (11) turned into a 1!")
              print(players_cards)
              print(player_total())
            else:
              print("You went over 21 and lost :(.")
              hit_me = False
          elif player_total() == 21:
            print("You have 21!")
            hit_me = False
          else:
            total = player_total()
            print(total)
        if choice == "n":
          hit_me = False
          #Cpu will hit me if total is equal to or under
          while cpu_cards_total < total:
            cpu_cards.append(random.choice(cards))
            cpu_cards_total = cpu_total()
            print(f"The computer has {cpu_cards}")
          print(winner())
      #Asks user to play again
      again = input("Do you want to play again? (y or n) ")
      if again == "n":
        play_again = False



