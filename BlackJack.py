# %%
print("Selamun aleykum Dunya")

# %%
print("Welcome to BlackJack Game Simulation")

# %%
# create a deck class 
# create a player class
# in the player class create a sum variable etc 
#

# %%
import random
Values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}
suits = ("Spade","Club","Diamond","Heart")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = Values[rank]
    
    def __str__(self):
        return ("{} of {}".format(self.rank,self.suit))

cardobject = Card("Spade"   ,"Ace")

# %%
class Deck:
    def __init__(self):
        self.card_list = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.card_list.append(card)
    def shuffle(self):
        random.shuffle(self.card_list)
        return self.card_list
    def deal_one(self):
        return self.card_list.pop()


# %%
class Player:
    def __init__(self, name, initial_bet_money):
        self.name = name
        self.initial_bet_money = initial_bet_money
        self.player_cards = []
        self.player_cards_sum = 0
    def Hit(self,new_card):
        self.player_cards.append(new_card)
    
    def Sum(self):
        if len(self.player_cards) != 0:
            self.player_cards_sum = 0
            for i in self.player_cards:
                self.player_cards_sum += i.value
        return self.player_cards_sum
    def Money(self, bet_money):
        self.initial_bet_money += bet_money
        return self.initial_bet_money
    def Print_card(self):
        print("{} Your Cards are : ".format(self.name))
        for i in self.player_cards:
            print(i)
        print("{} the total sum for your cards is {}".format(self.name,self.player_cards_sum))
        
            

# %%
# start game logic 

deck = Deck()
deck.shuffle()
dealer = Player("dealer",500)
player = Player("player",500)

for i in range(2):
    dealer.Sum()
    card = deck.deal_one()
    if card.rank == "Ace":
        if dealer.player_cards_sum <= 10 :
            card.value = 11
        else: 
            card.value = 1
    dealer.Hit(card)
    dealer.Sum()
for i in range(2):
    player.Sum()
    card = deck.deal_one()
    if card.rank == "Ace":
        if player.player_cards_sum <= 10 :
            card.value = 11
        else:
            card.value = 1
    player.Hit(card)
    player.Sum()


print("The Dealer's cards are : ")
print("{} +  Hidden ".format(dealer.player_cards[0]))

print("The player's Turn ")
player.Print_card()
print("This is your total amount that you can bet with : {}".format(player.initial_bet_money))
player_bet = float(input("Please enter the bet amount, make sure the amount is less than or equal to the total bet money that you have"))
print("You have selected {} Dollars as the bet amount".format(player_bet))
while player_bet<0 or player_bet>player.initial_bet_money:
    print("invalid amount entered , please make sure that the bet amount is between 0 and {}".format(player.initial_bet_money))
    player_bet = float(input())
choice = int(input(" Select your course of action :  \
                        1.) Hit \
                        2.) Stay "))
x=True
while choice == 1:
    card = deck.deal_one()
    if card.rank == "Ace":
        if player.player_cards_sum <= 10 :
            card.value = 11
        else:
            card.value = 1
    player.Hit(card)
    player.Sum()
    player.Print_card()
    if player.player_cards_sum > 21:
        print(""" BUST !!!! , YOU WENT OVER 21 POINTS, THE DEALER WINS!!!!!""")
        dealer.Money(player_bet)
        print("The dealer gets your bet, {} Dollars is now his, with a total of {}".format(player_bet,dealer.initial_bet_money))
        x= False
        break
    choice = int(input(" Select your course of action :  \
                            1.) Hit \
                            2.) Stay "))

while x:

    print("Your turn has ended, its now dealer's turn ")

    print("Disclosing the dealer's hand")
    dealer.Sum()
    dealer.Print_card()
    dealer_bet = random.randint(1,500)
    while True:
        while dealer.player_cards_sum < 18:
            card = deck.deal_one()
            if card.rank == "Ace":
                if dealer.player_cards_sum <= 10 :
                    card.value = 11
                else:
                    card.value = 1
            dealer.Hit(card)
            dealer.Sum()
            dealer.Print_card()
        if dealer.player_cards_sum > 21:
            print("BUST !!! , PLAYER WINS !!!")
            player.Money(dealer_bet)
            print("The player has now won the bet money of {} dollars , and has a total of {} dollars".format(dealer_bet,player.initial_bet_money))
            break
        elif dealer.player_cards_sum < player.player_cards_sum :
            print("The dealer has less than the player, hence dealer loses , the player wins, the dealer's bet goes to the player ")
            player.Money(dealer_bet)
            print("The player has now won the bet money of {} dollars , and has a total of {} dollars".format(dealer_bet,player.initial_bet_money))
            break
        elif player.player_cards_sum < dealer.player_cards_sum:
            print("The dealer has more points than the player, hence the dealer wins and gets the bet money of {} dollars and a total of {} dollars".format(player_bet,dealer.initial_bet_money))
            dealer.Money(player_bet)
            break
        else:
            print("The match has been tied , restart the game")
            break
    break
        
        

# %%


# %%


# %%
