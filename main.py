import random

# Global variables

game_number = 1
menu = '1. Get another card \n2. Hold hand \n3. Print statistics \n4. Exit\n\n'
cards = {
    'Ace': [1, 11],
    'Two': [2, 2],
    'Three': [3, 3],
    'Four': [4, 4],
    'Five': [5, 5],
    'Six': [6, 6],
    'Seven': [7, 7],
    'Eight': [8, 8],
    'Nine': [9, 9],
    'Ten': [10, 10],
    'Jack': [11, 10],
    'Queen': [12, 10],
    'King': [13, 10]
}

# cards = {
#     'Ace': [1, 11],
#     'Two': [2, 15],
#     'Three': [3, 15],
# }

# Functions



def deal_card():
    """This creates a list from the dictionary with card name, card number, and card value"""
    random_int = random.randint(0, len(cards) - 1)
    chosen_card_key = list(cards.keys())[random_int]
    chosen_card_value = list(cards.values())[random_int]
    return [chosen_card_key, chosen_card_value]

def player_new_card():
    """This picks a random card from the deck and creates a copy in a new list for the player, the original cards still remain in the deck"""
    [chosen_card_key, chosen_card_value] = deal_card()
    players_hand = [chosen_card_key, chosen_card_value]
    if chosen_card_value[0] not in [1,11,12,13]:
        print(f'Your card is a {chosen_card_value[0]}!')
    else:
        print(f'Your card is a {chosen_card_key.upper()}!')
    return players_hand

def dealer_new_card():
    """This picks a random card from the deck and creates a copy in a new list for the dealer, the original cards still remain in the deck"""
    [chosen_card_key, chosen_card_value ]= deal_card()
    dealers_hand = [chosen_card_key, chosen_card_value]
    return dealers_hand

def player_sum_hand(players_hand):
    """This sums up the value of the player's cards by iterating through the inner lists where the value is stored"""
    player_sum_hand = 0
    counter = 0
    for x in players_hand[1::2]:
        for y in x:
            counter += 1
            if not counter % 2:
               player_sum_hand += y
    if player_sum_hand > 21:
        if players_hand[0] == "Ace":
            player_sum_hand -= 10
        elif len(players_hand) > 2:
            if players_hand[2] == "Ace":
                player_sum_hand -= 10

    return player_sum_hand

def dealer_sum_hand(dealers_hand):
    """This sums up the value of the dealer's cards by iterating through the inner lists where the value is stored"""
    dealer_sum_hand = 0
    counter = 0
    for x in dealers_hand[1::2]:
        for y in x:
            counter += 1
            if not counter % 2:
               dealer_sum_hand += y
    if dealer_sum_hand > 21:
        if dealers_hand[0] == "Ace":
            dealer_sum_hand -= 10
        elif len(dealers_hand) > 2 :
            if dealers_hand[2] == "Ace":
                dealer_sum_hand -= 10
            
    return dealer_sum_hand
    
# Variables linked to functions


print(f'START GAME #{game_number}\n') 
   
players_hand = player_new_card()
dealers_hand = dealer_new_card()
print(type(deal_card()[0]))

# Print logic

carry_on = True

while carry_on:

    print("Player's hand:", player_sum_hand(players_hand))

    choices = input(menu)

    if choices == "1":
        players_hand += player_new_card()
        print("Your hand is:", player_sum_hand(players_hand))
        if dealer_sum_hand(dealers_hand) < 17:
            dealers_hand += dealer_new_card()
    elif choices == "2":
        dealers_hand += dealer_new_card()
        print("Temporary, dealer's hand:", dealers_hand[1::2])
        print("Temporary, dealer's hand is:", dealer_sum_hand(dealers_hand))
    elif choices == "4":
        carry_on = False
        print("GAME OVER")
        break

    if player_sum_hand(players_hand) == 21:
        print("BLACKJACK! You win!")
    elif player_sum_hand(players_hand) > 21 and dealer_sum_hand(dealers_hand) > 21:
        print("Both Dealer & Player exceeded 21 ... It's a tie no one wins!")
    elif player_sum_hand(players_hand) > 21:
        print("You exceeded 21! You lose.")
    elif dealer_sum_hand(dealers_hand) > 21:
        print("Dealer exceeded 21! You win!")
    elif player_sum_hand(players_hand) == dealer_sum_hand(dealers_hand):
        print("It's a tie! No one wins!")
    elif player_sum_hand(players_hand) > dealer_sum_hand(dealers_hand):
        print("You win, you have a higher score than dealer")
    elif player_sum_hand(players_hand) < dealer_sum_hand(dealers_hand):
        print("You lose, you have a lower score than dealer")
    else: print("UNKNOWN SCENARIO, NEED TO DEBUG!!!")

    # This if statement below was added as the index is out of range if player holds their hand

    score_text = f"which is a total score of: {player_sum_hand(players_hand)}, \nDealer's hand: {dealers_hand[0::2][0]} & {dealers_hand[0::2][1]}, which is a total score of: {dealer_sum_hand(dealers_hand)}"
    one_card_text = f"Player's hand: {players_hand[0::2][0]}"

    if len(players_hand) == 4:
        print(f"Player's hand: {players_hand[0::2][0]} & {players_hand[0::2][1]}, {score_text}")
    elif len(players_hand) == 2: 
        score_text, one_card_text
    
    print(players_hand, dealers_hand)
    print(len(players_hand), len(dealers_hand))
    

#TODO 2: Treat ACE as 1 or 11 (CHECK LOGIC)
#TODO 2: Print statistics of the game, keeping track of number of games played, number of wins/losses/ties, print out percentage of player wins to games played.
#TODO 3: If option 4 chosen, exit the game
#TODO 4: If other options chosen, throw error of Invalid input!  
#TODO 5: While loop to keep game looping 



