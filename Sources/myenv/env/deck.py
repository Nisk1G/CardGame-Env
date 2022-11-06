import card
import random

#player2のデッキ(後手)
def generateDeck(player):
    #デッキ用配列
    deck = []
    #デッキ作成
    deck.append(card.Unit("Unit1",player,3,3))
    deck.append(card.Unit("Unit2",player,1,5))
    deck.append(card.Unit("Unit3",player,4,2))

    return deck
#player1のデッキ(先手)
def generateDeckEnemy(player):
    #デッキ用配列
    deck = []
    #デッキ作成
    deck.append(card.Unit("Unit1",player,1,2))
    deck.append(card.Unit("Unit2",player,2,4))
    deck.append(card.Unit("Unit3",player,3,4))




    return deck

