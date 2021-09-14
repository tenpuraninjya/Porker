import random

deck = []
hands = []

#カードドロー
def Drow_card(num):
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
def Change_card(hands):
    try:
        x = list(map(int,input(f"交換したいカードの番号を１～３で入力してください（複数可）")))
        x.sort(reverse = True)
        print(x)
        for nums in x:
            while True:
                if nums == 1 or nums == 2 or nums == 3:
                    del hands[(nums-1)]
                    Drow_card(1)
                    break 
                elif nums == "q":
                    break
                else:
                    nums =input(f"正しい数字を入力してください。qで終わります。")
        return hands
    except:
        print(f"入力エラーで終了します")
        return hands

###  メイン  ###

#デッキの作成とシャッフル
mark = ["ダイヤ","ハート","スペード","クラブ"]
for i in mark:
    for j in range(1,14):
        deck.append([i,j])
        random.shuffle(deck)
