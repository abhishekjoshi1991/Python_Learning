
import random
suits=('Hearts','Spades','Diamonds','Clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

value={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=value[rank]
    def __str__(self):
        return  self.rank+ " of "+self.suit



class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle_card(self):
        random.shuffle(self.all_cards)

    def deal_one(self):#to remove one card from deck
        return self.all_cards.pop()


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = [] #initially player has no cards in hand

    def remove_one(self):#to remove single card from all_cards list
        return self.all_cards.pop(0)#to remove card from top of deck or left of list

    def add_cards(self,new_cards):#new cards to be added after each round
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards) #for adding multiple card objects
        else:
            self.all_cards.append(new_cards) #for adding single card

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name,len(self.all_cards))



#GAME SETUP
player_one=Player('one') #created player one
player_two=Player('two') #created player two

new_deck=Deck() #created new deck of 52 cards
new_deck.shuffle_card() #shuffled those 52 cards

'''split these 52 cards between two players,we are poping one card from
deal_one method and adding it to player one using below loop and then
again poping one card from deck_one method and adding it to player two

thats why we ran loop 26 times only
'''
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

#while game_on
round_num = 0 #counter to tally how many rounds are completed
while game_on:
    round_num+=1
    print('Rounds:',round_num)

    #to check any player is out of cards
    if len(player_one.all_cards)==0:
        print('player one out of cards, player two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('player two out of cards, player one wins!')
        game_on = False
        break

    #start of new round
    player_one_cards_in_hand = []
    player_one_cards_in_hand.append(player_one.remove_one())


    player_two_cards_in_hand = []
    player_two_cards_in_hand.append(player_two.remove_one())



    #while at_war situation
    at_war = True
    while at_war:
        if player_one_cards_in_hand[-1].value > player_two_cards_in_hand[-1].value:
            
