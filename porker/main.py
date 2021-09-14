import random
from combination import open_hands
from drowchange import drow_card
from drowchange import change_card

#準備
hands = []

#ゲーム本編
hands = drow_card(3,hands)
print(f"手持ちのカード：{hands}")
change = input(f"カードを交換しますか？y/n：")
if change == "y":
    hands = change_card(hands)
else:
    print("幸運を・・・")
    print()
print(f"【現在の手札は{hands}です。】")
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
print(f"あなたの役は【{result}】です!")

#中身の確認
#print(f"デッキの残りは{len(deck)}枚です")
