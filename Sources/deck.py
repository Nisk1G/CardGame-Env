import card
import cardeffect
import random


# player2のデッキ
def generateDeck(player):

    # デッキ用配列
    deck = []
    # デッキ作成
    '''
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    '''

    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))
    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))
    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))

    return deck
# player1のデッキ


def generateDeckEnemy(player):
    # デッキ用配列
    deck = []
    # デッキ作成 
    '''
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    deck.append(card.Unit("Unit1", player, 3, 3, 2))
    deck.append(card.Unit("Unit2", player, 2, 3, 3))
    deck.append(card.Unit("Unit3", player, 2, 4, 4))
    '''
    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))
    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))
    deck.append(card.Unit("spawner", player, 3, 3, 2, cardeffect.SpawnUnit))
    deck.append(card.Unit("damage2", player, 3, 3, 2, cardeffect.EnemyDamage2))
    deck.append(card.Unit("healer2", player, 3, 3, 2, cardeffect.PlayerHeal2))
    deck.append(card.Unit("drawer", player, 3, 3, 2, cardeffect.PlayerDraw))
    deck.append(card.Unit("attacker", player, 3, 3, 2, cardeffect.CanAttack))

    return deck
