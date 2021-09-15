import random

deck = []
#hands = []

#カードドロー
def drow_card(num,hands):
    for i in range(num):
        drow = deck.pop()
        hands.append(drow)
        print()
        print("-"*30)
        print(f"{drow}をドローした")
        print("-"*30)
        print()
    return hands

#カードチェンジ
def change_card(hands):
    try:
        x = list(map(int,input(f"交換したいカードの番号を１～３で入力してください（複数可）")))
        x.sort(reverse = True)
        #print(x)
        #print(hands)
        for nums in x:
           del hands[(nums-1)]
           hands = drow_card(1,hands)
           #nums =input(f"正しい数字を入力してください。qで終わります。")
        return hands
    except:
        print(f"入力エラーのためカード交換を終了します")
        return hands

#デッキの作成とシャッフル
mark = ["ダイヤ","ハート","スペード","クラブ"]
for i in mark:
    for j in range(1,14):
        deck.append([i,j])
        random.shuffle(deck)
        
        
        
        
#対戦相手のカードドロー
def op_drow_card(num,hands):
    for i in range(num):
        drow = deck.pop()
        hands.append(drow)
    return hands
