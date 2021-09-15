import random
from combination import open_hands
from drowchange import drow_card
from drowchange import op_drow_card
from drowchange import change_card

#準備
hands = []
ophands = []

### ゲーム本編 ###

# プレイヤー名の取得
#name = input(f"あなたの名前を入力してください。")
#print()
#opname = input(f"対戦相手の名前を入力してください")

#最初の手札

hands = drow_card(3,hands)
print(f"手持ちのカード：{hands}")
print()

#手札交換
while True:
    change = input(f"カードを交換しますか？y/n：")
    print()
    if change == "y":
        hands = change_card(hands)
        print(f"【現在の手札は{hands}です。】")
        print()
    else:
        print("カード交換を終了します。幸運を・・・")
        print()
        break

#役判定
print()
print("*"*70)
print(f"＞＞＞＞＞こ の 手 札 で 勝 負 し ま す ！＜＜＜＜＜")
print("*"*70)
print()
print()
print(hands)
print()
print()
result = open_hands(hands)
ophands = op_drow_card(3,ophands)
opresult = open_hands(ophands)
print(f"あなたの役は【{result}】です!")
print()
print()
print(f"対戦相手の役は【{opresult}]】です！")

#中身の確認
#print(f"デッキの残りは{len(deck)}枚です")
