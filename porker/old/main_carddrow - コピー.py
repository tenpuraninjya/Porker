import random
from combination import Open_hands

#イニシャライズ
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
    print(f"手持ちのカード：{hands}")
    print()

#カードチェンジ
def Change_card():
    nums = input(f"何枚目のカードを交換しますか？")
    while True:
        if  nums == "1" or nums == "2" or nums == "3":
            intnums = int(nums)
            del hands[(intnums-1)]
            Drow_card(1)
            break 
        elif nums == "q":
            break
        else:
            nums =input(f"正しい数字を入力してください。qで終わります。")

###  メイン  ###

#デッキの作成とシャッフル
mark = ["ダイヤ","ハート","スペード","クラブ"]
for i in mark:
    for j in range(1,14):
        deck.append([i,j])
        random.shuffle(deck)

#ゲーム本編
Drow_card(3)

change = input(f"カードを交換しますか？y/n：")
if change == "y":
    Change_card()
else:
    print("カード交換無しで勝負に挑みます！")

print(f"【現在の手札は{hands}です。】")
print()
print("*"*70)
print(f"＞＞＞＞＞こ の 手 札 で 勝 負 し ま す ！＜＜＜＜＜")
print("*"*70)
print()
result = Open_hands(hands)
print(f"あなたの役は【{result}】です")

#中身の確認
print(f"デッキの残りは{len(deck)}枚です")
