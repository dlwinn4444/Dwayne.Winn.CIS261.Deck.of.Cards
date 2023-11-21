#Dwayne Winn CIS261

import random

class cards:
   def __Init(self, rank, suit):
      self.rank = rank
      self.suit = suit
      
class Deck:
   def __init__(self):
      self.ranks = ['ACE','2','3','4','5','6','7','8','9','10','Jack','Gueen','King']
      self.suits = ['Hearts','Diamonds','Clubs','Spades']
      self.reset()
   def reset(self):
      self.deck = [card(rank, suit) for suit in self.suits for rank in self.ranks]
      
   def shuffle(self):
       random.shuffle(self.deck)
       
    def deal(self):
      if len(self, deck) == 0
         return None
      return.self.deck.pop()
print("Welcome to the card dealer")
print()
print("There is 52 cards in the deck")

deck = Deck()

deck.shuffle()
num_cards = int(input("how many cards would you like?: "))
dealt.cards = []

for _ in 


       

      