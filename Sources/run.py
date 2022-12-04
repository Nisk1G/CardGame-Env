import player2
import deck
import card
import sys

#デッキの初期化
def initdecks(player):
    #デッキ生成
    player.deck = deck.generateDeck(player)
    #デッキのシャッフル
    player.shuffle()
    #対戦相手にも同じこと
    player.enemy.deck = deck.generateDeckEnemy(player.enemy)
    player.enemy.shuffle()

#ゲーム開始時のドロー
def inithands(player):
    #敵味方3枚ずつドロー
    player.draw()
    player.draw()
    player.draw()
    player.enemy.draw()
    player.enemy.draw()
    player.enemy.draw()
    #player.enemy.draw()
    #player.enemy.draw()


#カードのis_used状態をリセット（ターン処理で呼ばれる)
def resetuse(player):
    for played_card in player.is_played:
        if played_card.attack == 0 and played_card.is_used == card.Card.use:
            played_card.is_used = True
        else:
            played_card.is_used = False

#プレイヤーのコストUpdate処理 (ターン処理で呼ばれる)
def updatecost(player):
    if player.turnmaxcost < player.maxcost:
        player.turnmaxcost += 1
    player.cost = player.turnmaxcost
    print("updated cost")
    print(player.name + ":" + str(player.cost))

def doTurn(player):
    print ("")
    print ("--")

    #敵が先手の場合

    #敵のカードドロー
    player.enemy.draw()
    #敵がデッキ切れ起こしたらreturn
    if player.enemy.is_deckend:
        return
    #敵のカードプレイ
    log = player.enemy.playcard()
    log += player.enemy.usecard()
    #敵のresetuse
    resetuse(player.enemy)
    #敵のupdatecost
    updatecost(player.enemy)
    
    #敵の番でHP切れたらretrun
    if player.is_dead:
        return

    print ("")
    print ("--")
    #自分も同じことする
    player.draw()
    #自分がデッキ切れ起こしたらreturn 
    if player.is_deckend:
        return
    log = player.playcard()
    log += player.usecard()
    resetuse(player)
    updatecost(player)

def play():
    player = player2.Player2()

    initdecks(player)

    inithands(player)

    resetuse(player)
    resetuse(player.enemy)

    while True:
        #player1の場を表示
        player.enemy.printisplayed()

        #player2の場を表示
        player.printisplayed()

        doTurn(player)  

        #勝利条件
        #敵の勝利条件
        if player.is_dead == True or player.is_deckend == True:
            print(player.enemy.name + "Win!!")
            sys.exit(player.enemy.name + "Win!!")
        elif player.enemy.is_dead == True or player.enemy.is_deckend == True:
            print(player.name + "Win!!")
            sys.exit(player.name + "Win!!")

if __name__ == '__main__':
    print ("")
    print ("-----------------------")

    play()


    




